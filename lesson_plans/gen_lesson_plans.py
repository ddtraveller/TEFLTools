import anthropic
import os
import re

# Initialize the Anthropic client
client = anthropic.Anthropic()

def extract_units(content):
    """Extract individual units from the content."""
    units = re.findall(r'### Unit \d+:.*?(?=### Unit|\Z)', content, re.DOTALL)
    return [unit.strip() for unit in units]

def generate_lesson_plan(unit):
    """Generate a lesson plan for a given unit using Claude."""
    prompt = f"""Given the following unit from a syllabus:
{unit}
Please provide a detailed lesson plan for this unit, including:
1. Resources needed for the lesson
2. Lesson objectives
3. Warm-up activity
4. Pre-teaching of key vocabulary or concepts
5. Presentation of the main lesson content
6. Practice activities for students
7. Production tasks or activities
8. Wrap-up and review
9. Homework assignment
10. Key vocabulary definitions
Format the output as Markdown, with clear section headers for each part of the lesson plan."""
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
        print(f"Error generating lesson plan: {str(e)}")
        return ""

def create_lesson_plan_file(unit_number, lesson_plan):
    """Create a file for each unit's lesson plan."""
    filename = f"Unit{unit_number}_Lesson_Plan.md"
    try:
        with open(filename, 'w') as file:
            file.write(lesson_plan)
        print(f"Created file: {filename}")
    except Exception as e:
        print(f"Error creating file {filename}: {str(e)}")

def main():
    try:
        # Read the syllabus from a file
        with open('syllabus.md', 'r') as file:
            content = file.read()
        print(f"Successfully read syllabus.md. Content length: {len(content)} characters")
        
        # Extract individual units
        units = extract_units(content)
        print(f"Extracted {len(units)} units from the syllabus")
        
        # Process each unit
        for i, unit in enumerate(units, 1):
            print(f"Processing Unit {i}...")
            lesson_plan = generate_lesson_plan(unit)
            if lesson_plan:
                create_lesson_plan_file(i, lesson_plan)
            else:
                print(f"No lesson plan generated for Unit {i}")
        
        print("Script execution completed.")
    except FileNotFoundError:
        print("Error: syllabus.md file not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()