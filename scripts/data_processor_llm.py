import os
import json
from typing import List, Dict

def read_json_file(file_path: str) -> Dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file_path}: {str(e)}")
        return None
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None

def process_quiz_file(file_path: str) -> List[Dict]:
    data = read_json_file(file_path)
    if data is None:
        return []
    
    processed_data = []
    try:
        for question in data.get('questions', []):
            processed_question = {
                'context': data.get('title', ''),
                'question': question.get('question', ''),
                'choices': question.get('choices', []),
                'answer': question.get('answer', '')
            }
            processed_data.append(processed_question)
    except Exception as e:
        print(f"Error processing questions in file {file_path}: {str(e)}")
    
    return processed_data

def process_quiz_folder(folder_path: str) -> List[Dict]:
    all_data = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                try:
                    file_data = process_quiz_file(file_path)
                    all_data.extend(file_data)
                    print(f"Successfully processed: {file_path}")
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")
    return all_data

def save_processed_data(data: List[Dict], output_file: str):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to {output_file}: {str(e)}")

def main():
    quiz_folder = '/home/ubuntu/environment/TEFLTools/quizzes'  # Replace with the actual path
    output_file = 'processed_quiz_data.json'
    
    processed_data = process_quiz_folder(quiz_folder)
    save_processed_data(processed_data, output_file)
    
    print(f"Processed {len(processed_data)} questions from quiz files.")

if __name__ == "__main__":
    main()