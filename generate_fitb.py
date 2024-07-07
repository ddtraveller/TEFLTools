import os
import json
import anthropic
import re

client = anthropic.Anthropic()

def find_matching_reading(support_file, readings_dir):
    course_name = os.path.basename(os.path.dirname(support_file))
    unit_name = os.path.basename(support_file).replace("_Support_Material.md", "_Reading.md")
    reading_file = os.path.join(readings_dir, course_name, unit_name)
    return reading_file if os.path.exists(reading_file) else None

def clean_text(s):
    # Remove or replace special characters that could interfere with JSON formatting
    s = s.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
    s = s.replace('"', '\\"')
    # Remove any other non-printable characters
    s = ''.join(char for char in s if ord(char) >= 32 or char in '\n\r\t')
    return s

def process_files_with_anthropic(support_file, reading_file):
    with open(support_file, 'r', encoding='utf-8') as f:
        support_content = f.read()
    
    with open(reading_file, 'r', encoding='utf-8') as f:
        reading_content = f.read()

    prompt = f"""Task: Create a fill-in-the-blank exercise based on the given reading and support material.

Support Material:
{support_content}

Reading:
{reading_content}

Instructions:
1. Extract 10 key vocabulary words from the support material.
2. Create a version of the reading with these vocabulary words replaced by [BLANK_1], [BLANK_2], etc.
3. Provide a list of the extracted vocabulary words in the order they appear in the modified reading.

Format your response as follows:
MODIFIED_READING:
(Your modified reading text here)

VOCABULARY:
1. (First vocabulary word)
2. (Second vocabulary word)
...
10. (Tenth vocabulary word)

Do not include any other text or explanation in your response.
"""

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
    
    response_text = message.content[0].text
    
    # Extract modified reading and vocabulary from the response
    reading_match = re.search(r'MODIFIED_READING:\n(.*?)\n\nVOCABULARY:', response_text, re.DOTALL)
    vocab_match = re.findall(r'\d+\.\s*(.+)', response_text)

    if reading_match and vocab_match:
        modified_reading = clean_text(reading_match.group(1).strip())
        vocabulary = {f"[BLANK_{i+1}]": clean_text(word.strip()) for i, word in enumerate(vocab_match)}

        # Create JSON structure
        json_content = {
            "reading": modified_reading,
            "vocabulary": vocabulary
        }

        return json.dumps(json_content, ensure_ascii=False, indent=2)
    else:
        print(f"Error: Could not extract reading or vocabulary from Anthropic's response for {support_file}")
        return None

def main():
    lesson_plans_dir = 'lesson_plans'
    readings_dir = 'Readings'
    quizzes_fitb_dir = 'quizzes_fitb'

    for root, dirs, files in os.walk(lesson_plans_dir):
        for file in files:
            if file.endswith("_Support_Material.md"):
                support_file = os.path.join(root, file)
                reading_file = find_matching_reading(support_file, readings_dir)
                
                if reading_file and os.path.exists(reading_file):
                    json_content = process_files_with_anthropic(support_file, reading_file)
                    
                    if json_content:
                        course_name = os.path.basename(os.path.dirname(support_file))
                        output_dir = os.path.join(quizzes_fitb_dir, course_name)
                        if not os.path.exists(output_dir):
                            os.makedirs(output_dir)
                        
                        output_file = os.path.join(output_dir, file.replace("_Support_Material.md", "_FITB.json"))
                        
                        with open(output_file, 'w', encoding='utf-8') as f:
                            f.write(json_content)
                        print(f"Created {output_file}")
                    else:
                        print(f"Failed to generate valid JSON for {support_file}")
                else:
                    print(f"No matching reading file found for {support_file}")

if __name__ == "__main__":
    main()