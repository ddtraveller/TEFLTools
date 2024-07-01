import anthropic
import os

# Initialize the Anthropic client
client = anthropic.Anthropic()

def generate_syllabus(project_info):
    """Generate a syllabus based on the project information using Claude."""
    prompt = f"""Given the following project information:
{project_info}
Please do the following:
1. Synthesize the key points and goals of the project
2. Localize the content for Timor Leste, considering cultural context and appropriateness
3. Create a well-structured syllabus for a program, including:
   - Course overview and objectives
   - Weekly or unit-based structure with topics and activities
   - Required resources (books, materials)
   - Suggested items to cover
   - Ideas for practical experience and community engagement
   - Resources
Format the output as Markdown, with clear headings and subheadings for each section."""
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
        print(f"Error generating syllabus: {str(e)}")
        return ""

def create_syllabus_file(syllabus_content):
    """Create a file to store the generated syllabus."""
    filename = "Syllabus.md"
    try:
        with open(filename, 'w') as file:
            file.write(syllabus_content)
        print(f"Created file: {filename}")
    except Exception as e:
        print(f"Error creating file {filename}: {str(e)}")

def main():
    try:
        # Read the project information from a file
        with open('paste.txt', 'r') as file:
            project_info = file.read()
        print(f"Successfully read paste.txt. Content length: {len(project_info)} characters")

        # Generate the syllabus
        syllabus_content = generate_syllabus(project_info)
        if syllabus_content:
            create_syllabus_file(syllabus_content)
        else:
            print("Syllabus generation failed.")

        print("Script execution completed.")
    except FileNotFoundError:
        print("Error: paste.txt file not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()