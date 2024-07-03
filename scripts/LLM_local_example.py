from gpt4all import GPT4All

def initialize_model(model_path):
    print(f"Loading GPT4All model from {model_path}")
    model = GPT4All(model_path)
    print("GPT4All model loaded.")
    return model

def generate_response(model, prompt, max_tokens=200):
    response = model.generate(prompt, max_tokens=max_tokens)
    return response

# Specify the path to your downloaded GPT4All model
model_path = "path/to/your/gpt4all_model.bin"

# Initialize the model
model = initialize_model(model_path)

# Main loop
while True:
    question = input("Ask a question (or type 'quit' to exit): ")
    if question.lower() == 'quit':
        break
    
    enriched_prompt = f"You are an AI assistant. Use the following context to answer the question:\n\nQuestion: {question}\nAnswer:"
    response = generate_response(model, enriched_prompt)
    print(response)

print("Thank you for using GPT4All. Goodbye!")