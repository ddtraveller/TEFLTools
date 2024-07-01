import anthropic
import os
import json
import re
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the Anthropic client
client = anthropic.Anthropic()

def load_file_content(file_path):
    """Load and return the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        return ""

def generate_quiz(module_content, context_files, attempt=1):
    """Generate a quiz JSON using Claude."""
    context = "\n\n".join([f"File: {file}\n\nContent:\n{content}" for file, content in context_files.items()])
    prompt = f"""Given the following module content and additional context files from a course:

Module Content:
{module_content}

Additional Context:
{context}

Please generate a JSON file containing a multiple-choice quiz based on this module's content. The JSON structure should be as follows:

{{
  "title": "Module Title",
  "questions": [
    {{
      "question": "Question text",
      "choices": [
        "Choice A", 
        "Choice B",
        "Choice C",
        "Choice D"  
      ],
      "answer": "Correct choice"
    }},
    // ... more questions ...
  ]
}}

Generate at least 30 questions covering key concepts from the module. Ensure that the questions are challenging, relevant to the material, and cover a wide range of topics from the module content.

IMPORTANT: Ensure that your response is a valid JSON object. Do not include any text before or after the JSON object."""

    if attempt > 1:
        prompt += "\n\nThe previous attempt resulted in invalid JSON. Please double-check that your response is a valid JSON object."

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4000,
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        response = message.content[0].text if message.content else ""
        
        # Log the raw response for debugging
        logging.info(f"Raw response from AI (attempt {attempt}):\n{response}")
        
        return response
    except Exception as e:
        logging.error(f"Error generating quiz (attempt {attempt}): {str(e)}")
        return ""

def validate_and_process_quiz(quiz_json, module_name, attempt=1):
    """Validate the quiz JSON and ensure it has at least 30 questions."""
    try:
        # Try to parse the JSON
        quiz_data = json.loads(quiz_json)
        
        # Validate the structure
        if not isinstance(quiz_data, dict):
            raise ValueError("Root element is not an object")
        if "title" not in quiz_data or not isinstance(quiz_data["title"], str):
            raise ValueError("Missing or invalid 'title' field")
        if "questions" not in quiz_data or not isinstance(quiz_data["questions"], list):
            raise ValueError("Missing or invalid 'questions' field")
        
        questions = quiz_data["questions"]
        
        if len(questions) < 30:
            logging.warning(f"Generated quiz for {module_name} has only {len(questions)} questions (attempt {attempt}). Requesting more...")
            return None
        
        # Validate each question
        for i, q in enumerate(questions):
            if not isinstance(q, dict):
                raise ValueError(f"Question {i} is not an object")
            if "question" not in q or not isinstance(q["question"], str):
                raise ValueError(f"Question {i} is missing or has invalid 'question' field")
            if "choices" not in q or not isinstance(q["choices"], list) or len(q["choices"]) != 4:
                raise ValueError(f"Question {i} is missing or has invalid 'choices' field")
            if "answer" not in q or not isinstance(q["answer"], str):
                raise ValueError(f"Question {i} is missing or has invalid 'answer' field")
            if q["answer"] not in q["choices"]:
                raise ValueError(f"Question {i} has an answer that is not in the choices")
        
        return json.dumps(quiz_data, indent=2)
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error for {module_name} (attempt {attempt}): {str(e)}")
    except ValueError as e:
        logging.error(f"Validation error for {module_name} (attempt {attempt}): {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error processing quiz for {module_name} (attempt {attempt}): {str(e)}")
    
    return None

def process_file(file_path):
    """Process a single file."""
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    module_content = load_file_content(file_path)
    
    context_files = {}
    module_dir = os.path.dirname(file_path)
    for file in os.listdir(module_dir):
        if file.endswith(('.md', '.txt')) and file != os.path.basename(file_path):
            context_file_path = os.path.join(module_dir, file)
            context_files[file] = load_file_content(context_file_path)
    
    quiz_json = None
    attempts = 0
    max_attempts = 3

    while quiz_json is None and attempts < max_attempts:
        attempts += 1
        raw_quiz_json = generate_quiz(module_content, context_files, attempts)
        quiz_json = validate_and_process_quiz(raw_quiz_json, module_name, attempts)

    if quiz_json:
        output_dir = os.path.abspath(os.path.join(os.getcwd(), '..', 'quizzes'))
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"{module_name}_quiz.json")
        
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(quiz_json)
            logging.info(f"Created quiz file: {output_file}")
        except Exception as e:
            logging.error(f"Error writing quiz file {output_file}: {str(e)}")
    else:
        logging.error(f"Failed to generate a valid quiz with at least 30 questions for {module_name} after {max_attempts} attempts.")

def process_directory(directory):
    """Recursively process files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.txt')) and any(keyword in file.lower() for keyword in ['unit', 'week', 'module']):
                file_path = os.path.join(root, file)
                logging.info(f"Processing {file_path}...")
                process_file(file_path)

def main():
    input_dir = input("Enter the directory to process: ")
    input_dir = os.path.abspath(input_dir)
    
    if not os.path.exists(input_dir):
        logging.error(f"Error: Input directory not found at {input_dir}")
        return
    
    process_directory(input_dir)
    
    logging.info("Script execution completed.")

if __name__ == "__main__":
    main()