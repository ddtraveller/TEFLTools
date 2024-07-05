import json
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import Dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# Set your Hugging Face access token here
ACCESS_TOKEN = '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'

def load_dataset(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def prepare_data(data):
    prepared_data = []
    for item in data:
        text = f"<start_of_turn>user\nContext: {item['context']}\nQuestion: {item['question']}\nChoices: {', '.join(item['choices'])}\nProvide the correct answer and a brief explanation.<end_of_turn>\n<start_of_turn>model\nThe correct answer is: {item['answer']}. Explanation: <end_of_turn>\n"
        prepared_data.append({"text": text})
    return prepared_data

def tokenize_function(examples, tokenizer):
    return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)

def main():
    # Load and prepare data
    raw_data = load_dataset('processed_quiz_data.json')
    prepared_data = prepare_data(raw_data)
    
    # Create a Hugging Face Dataset
    dataset = Dataset.from_list(prepared_data)

    # Load pre-trained model and tokenizer with authentication
    model_name = "google/gemma-7b-it"
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=ACCESS_TOKEN)
    model = AutoModelForCausalLM.from_pretrained(model_name, 
                                                 token=ACCESS_TOKEN,
                                                 device_map="auto", 
                                                 torch_dtype=torch.bfloat16,
                                                 use_cache=False)

    # Prepare the model for k-bit training
    model = prepare_model_for_kbit_training(model)

    # Set up LoRA configuration
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )

    # Get the PEFT model
    model = get_peft_model(model, lora_config)

    # Tokenize the dataset
    tokenized_dataset = dataset.map(lambda examples: tokenize_function(examples, tokenizer), batched=True, remove_columns=dataset.column_names)

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir="./gemma_7b_fine_tuned",
        per_device_train_batch_size=1,
        gradient_accumulation_steps=4,
        num_train_epochs=3,
        learning_rate=2e-5,
        bf16=True,  # Use bfloat16 precision
        save_steps=100,
        logging_steps=10,
        save_total_limit=2,
    )

    # Create Trainer instance
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    # Start training
    trainer.train()

    # Save the model
    model.save_pretrained("./gemma_7b_fine_tuned")
    tokenizer.save_pretrained("./gemma_7b_fine_tuned")

if __name__ == "__main__":
    main()