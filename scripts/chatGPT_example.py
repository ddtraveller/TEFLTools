import gpt4all

def initialize_gpt4all(model_path):
    print("Loading GPT4All model...")
    model = gpt4all.GPT4All(model_path)
    print("GPT4All model loaded.")
    return model
    
def generate_response(model, prompt, max_tokens=2000, continuation_attempts=3):
    full_response = ""
    for _ in range(continuation_attempts):
        with model.chat_session():
            response = model.generate(prompt=prompt, temp=0.7, max_tokens=max_tokens)
        full_response += response
        
        if response.strip().endswith(('.', '!', '?')):
            break
        else:
            prompt = f"{prompt}\n{response}\nPlease continue:"
    
    return full_response

question = input("Ask a question?: ")
# Global variable for model path
model_path = "orca-mini-3b-gguf2-q4_0.gguf"
model = initialize_gpt4all(model_path)    
enriched_prompt = f"You are an AI assistant. Use the following context to answer the question:\n\nQuestion: {question}\nAnswer:"
response = generate_response(model, enriched_prompt)   
print(response)