import anthropic
import os
import re

# Initialize the Anthropic client
client = anthropic.Anthropic()

def extract_weeks(content):
    """Extract individual weeks from the content."""
    weeks = re.findall(r'### Week \d+-\d+:.*?(?=### Week|\Z)', content, re.DOTALL)
    return [week.strip() for week in weeks]

def generate_lesson_resources(week):
    """Generate resources for a given week using Claude."""
    prompt = f"""Given the following week's plan from a fiction writing course syllabus:

{week}

Please provide detailed resources for this week's lessons, including:
1. Full text of any mentioned excerpts or short stories
2. Detailed lecture notes for each topic
3. Discussion questions for each topic
4. Writing exercise instructions
5. Assignment details
6. Any additional relevant materials or examples

Format the output as Markdown, with clear section headers for each resource type and subtopics within the week."""

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
        print(f"Error generating resources: {str(e)}")
        return ""

def create_week_file(week_number, week_content, resources):
    """Create a file for each week with its content and resources."""
    filename = f"Week_{week_number}.md"
    try:
        with open(filename, 'w') as file:
            file.write(f"# {week_content.split(':')[0].strip()}\n\n")
            file.write(week_content)
            file.write("\n\n## Week Resources\n\n")
            file.write(resources)
        print(f"Created file: {filename}")
    except Exception as e:
        print(f"Error creating file {filename}: {str(e)}")

def main():
    try:
        # Read the syllabus from a file
        with open('lesson_plans.md', 'r') as file:
            content = file.read()
        print(f"Successfully read lesson_plans.md. Content length: {len(content)} characters")

        # Extract individual weeks
        weeks = extract_weeks(content)
        print(f"Extracted {len(weeks)} weeks from the content")

        # Process each week
        for i, week in enumerate(weeks, 1):
            print(f"Processing Week {i}...")
            resources = generate_lesson_resources(week)
            if resources:
                create_week_file(i, week, resources)
            else:
                print(f"No resources generated for Week {i}")

        print("Script execution completed.")
    except FileNotFoundError:
        print("Error: lesson_plans.md file not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()