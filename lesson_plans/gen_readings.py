import anthropic
import os
import re

# Initialize the Anthropic client
client = anthropic.Anthropic()

def extract_lesson_topic(lesson_plan):
    """Extract the lesson topic from the lesson plan."""
    match = re.search(r'# Lesson Plan: (.*)', lesson_plan)
    if match:
        return match.group(1)
    else:
        return "Unknown Topic"

def generate_reading(lesson_plan, attempt=1):
    """Generate a reading about the subject of the lesson plan using Claude."""
    topic = extract_lesson_topic(lesson_plan)
    prompt = f"""Given the following lesson plan:

{lesson_plan}

Please write a paper that covers the subject of this lesson plan. The paper should focus on the topic itself, "{topic}", rather than the teaching aspects of the lesson. Take on the role of an author writing an informative article about {topic} for a general audience. The paper should be well-structured, with an introduction, main body discussing the key points of {topic}, and a conclusion. Use a formal writing style and include relevant examples and facts to support the main ideas.
"""

    if attempt > 1:
        prompt += "\n\nThe previous attempt did not fully cover the subject. Please try again, ensuring the paper thoroughly explores the topic and provides a comprehensive overview."

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
        return message.content[0].text if message.content else ""
    except Exception as e:
        print(f"Error generating reading (attempt {attempt}): {str(e)}")
        return ""

def create_reading_file(lesson_name, reading):
    """Create a file for each lesson's reading."""
    filename = f"{lesson_name}_Reading.md"
    output_dir = os.path.join(os.getcwd(), 'Readings')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(reading)
        print(f"Created file: {file_path}")
    except Exception as e:
        print(f"Error creating file {file_path}: {str(e)}")

def process_file(file_path):
    """Process a single lesson plan file."""
    lesson_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, 'r', encoding='utf-8') as file:
        lesson_plan = file.read()

    reading = None
    attempts = 0
    max_attempts = 3

    while reading is None and attempts < max_attempts:
        attempts += 1
        reading = generate_reading(lesson_plan, attempts)

    if reading:
        create_reading_file(lesson_name, reading)
    else:
        print(f"Failed to generate a reading for {lesson_name} after {max_attempts} attempts.")

def process_directory(directory):
    """Recursively process lesson plan files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('_Lesson_Plan.md'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                process_file(file_path)

def main():
    input_dir = input("Enter the directory containing lesson plans: ")
    input_dir = os.path.abspath(input_dir)

    if not os.path.exists(input_dir):
        print(f"Error: Input directory not found at {input_dir}")
        return

    process_directory(input_dir)

    print("Script execution completed.")

if __name__ == "__main__":
    main()