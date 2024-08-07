import anthropic
import os
import re
import requests
from bs4 import BeautifulSoup
import time
import json
import PyPDF2
import tiktoken
import shutil
import zipfile
import xml.etree.ElementTree as ET

# Initialize the Anthropic client
# export ANTHROPIC_API_KEY='your_api_key_here'
client = anthropic.Anthropic()

def clean_name(name):
    """Clean the name to be safe for file systems and folder names."""
    cleaned = re.sub(r'[^\w\-_\. ]', '', name)
    cleaned = re.sub(r'\s+', '_', cleaned)
    return cleaned.lower()

def create_directory(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Created directory: {path}")

def read_docx(path):
    """Read text from a .docx file."""
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = ET.XML(xml_content)
    
    paragraphs = []
    for paragraph in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p'):
        texts = [node.text for node in paragraph.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t') if node.text]
        if texts:
            paragraphs.append(''.join(texts))
    
    return '\n\n'.join(paragraphs)

def read_file_content(file_path):
    """Read content from PDF, TXT, MD, or DOCX files."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == '.pdf':
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            return "\n".join([page.extract_text() for page in pdf_reader.pages])
    elif ext in ['.txt', '.md']:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    elif ext == '.docx':
        try:
            return read_docx(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            return ""
    else:
        print(f"Unsupported file format: {file_path}")
        return ""

def write_to_file(content, file_path):
    """Write content to a file and print confirmation."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Written file: {file_path}")

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

def truncate_to_token_limit(text: str, max_tokens: int = 199999) -> str:
    """Truncates the text to fit within the specified token limit."""
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return encoding.decode(tokens[:max_tokens])

def extract_weeks(content):
    """Extract individual weeks from the content."""
    weeks = re.findall(r'#### Week \d+:.*?(?=#### Week|\Z)', content, re.DOTALL | re.IGNORECASE)
    print(f"Found {len(weeks)} weeks")
    if len(weeks) == 0:
        print("Syllabus structure:")
        print(re.findall(r'#{1,4} .*', content))  # Print all headings
    return [week.strip() for week in weeks]

def extract_modules(content):
    """Extract individual modules from the content."""
    modules = re.findall(r'## Module \d+:.*?(?=## Module|\Z)', content, re.DOTALL | re.IGNORECASE)
    print(f"Found {len(modules)} modules")
    return [module.strip() for module in modules]

def extract_units(content):
    """Extract individual units from the content."""
    units = re.findall(r'### Unit \d+\.\d+:.*?(?=### Unit|\Z)', content, re.DOTALL | re.IGNORECASE)
    print(f"Found {len(units)} units")
    return [unit.strip() for unit in units]

def generate_lesson_plan(unit, syllabus, truncated_info):
    """Generate a lesson plan for a given learning unit using Claude."""
    prompt = f"""Given the following project information:
{truncated_info}
And given the following learning unit from a syllabus:
{unit}

And the complete syllabus for context:
{syllabus}

Please provide a detailed lesson plan for this learning unit, including:
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
Format the output as Markdown, with clear section headers for each part of the lesson plan.
Don't add any commentary at the top, like 'Here is a lesson plan...'"""
    
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
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def generate_lesson_resources(week, syllabus, lesson_plan):
    """Generate resources for a given week using Claude."""
    prompt = f"""Given the following week's plan from a course syllabus:

{week}

And the complete syllabus for context:
{syllabus}

And the lesson plan for this week:
{lesson_plan}

Please provide detailed resources for this week's lessons, including:
1. Full text of any mentioned excerpts or short stories
2. Detailed lecture notes for each topic
3. Discussion questions for each topic
4. Writing exercise instructions
5. Assignment details
6. Any additional relevant materials or examples

Format the output as Markdown, with clear section headers for each resource type and subtopics within the week.
Don't add any commentary at the top, like 'Here are the resources...'"""

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
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def fetch_and_clean_url_content(url):
    """Fetch content from URL and clean it using Anthropic."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        text_content = soup.get_text()
        
        prompt = f"Clean and format the following text content from a webpage, removing any irrelevant information and preserving only the main text content:\n\n{text_content[:2000]}..."

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=2000,
            temperature=0,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        time.sleep(2)  # Pause for 2 seconds after Anthropic call
        return message.content[0].text if message.content else ""
    except Exception as e:
        print(f"Error fetching or cleaning URL content: {str(e)}")
        return ""

def process_additional_resource(week_name, resource, syllabus, lesson_resources):
    """Process an additional resource using Anthropic."""
    if '[Link to audio' in resource or '[Link to video' in resource:
        prompt = f"For a course in {week_name}, please provide a text-based alternative or transcript for the following audio/video resource: {resource}"
    elif resource.startswith('[') and resource.endswith(']'):
        prompt = f"For a course in {week_name}, please create or find content related to: {resource}"
    else:
        prompt = f"For a course in {week_name}, please create a comprehensive resource on the following topic: {resource}"

    prompt += f"\n\nConsider the following context:\nSyllabus:\n{syllabus}\n\nLesson Resources:\n{lesson_resources}"
    prompt += "Do NOT add any commentary along with the output like, 'Here's a comprehensive resource...'"

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=3000,
        temperature=0.2,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def generate_reading(lesson_plan, syllabus, lesson_resources, truncated_info):
    """Generate a reading about the subject of the lesson plan using Claude."""
    topic = re.search(r'# Lesson Plan: (.*)', lesson_plan).group(1) if re.search(r'# Lesson Plan: (.*)', lesson_plan) else "Unknown Topic"
    prompt = f"""Given this information: 
{truncated_info}
Given the following lesson plan:

{lesson_plan}

And the lesson resources:
{lesson_resources}

Please write a paper that covers the subject of this lesson plan. The paper should focus on the topic itself, "{topic}", rather than the teaching aspects of the lesson. Take on the role of an author writing an informative article about {topic} for a general audience. The paper should be well-structured, with an introduction, main body discussing the key points of {topic}, and a conclusion. Use a formal writing style and include relevant examples and facts to support the main ideas.
Don't add any commentary at the top, like 'Here is a reading...'
Don't add any verbiage at the top of the output before the paper.
Do NOT add anything like, "Based on the provided syllabus and context for the course..."
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
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def generate_quiz(module_content, context_files, truncated_info):
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
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def generate_activities(lesson_plan, syllabus):
    """Generate activities for a lesson using Claude."""
    prompt = f"""Given the following lesson plan:

{lesson_plan}

And the complete syllabus for context:
{syllabus}

Please create a set of engaging activities for this lesson, including:
1. Warm-up activities
2. Main lesson activities
3. Group work or pair work tasks
4. Individual practice exercises
5. Cool-down or wrap-up activities

Ensure that the activities are appropriate for the lesson content, engaging for students, and help reinforce the key concepts of the lesson. Format the output as Markdown, with clear section headers for each type of activity.
Don't add any commentary at the top, like 'Here is an activity...'"""

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=3000,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def generate_support_material(lesson_plan, syllabus):
    """Generate support material for a lesson using Claude."""
    prompt = f"""Given the following lesson plan:

{lesson_plan}

And the complete syllabus for context:
{syllabus}

Please create support material for this lesson, including:
1. Key vocabulary list with definitions
2. Visual aids or diagrams (described in text)
3. Handouts or worksheets (content described)
4. Additional resources for further reading or practice
5. Tips for teachers on potential challenges and how to address them

Format the output as Markdown, with clear section headers for each type of support material."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=3000,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    time.sleep(2)  # Pause for 2 seconds
    return message.content[0].text if message.content else ""

def extract_learning_units(content):
    """Extract individual learning units from the content."""
    units = re.findall(r'## Learning Unit \d+:.*?(?=## Learning Unit|\Z)', content, re.DOTALL | re.IGNORECASE)
    print(f"Found {len(units)} learning units")
    if len(units) == 0:
        print("Syllabus structure:")
        print(re.findall(r'#{1,3} .*', content))  # Print all headings
    return [unit.strip() for unit in units]

def move_files_to_tefltools(base_dir, course_name):
    """Move generated files to the TEFLTools repository structure."""
    tefltools_dir = "/home/ubuntu/environment/TEFLTools"
    
    # Move syllabus (no subfolder)
    syllabus_src = f"{base_dir}/syllabus/{course_name}.md"
    syllabus_dst = f"{tefltools_dir}/syllabus/{course_name}.md"
    shutil.move(syllabus_src, syllabus_dst)
    print(f"Moved syllabus to {syllabus_dst}")

    # Move lesson plans and support material
    lesson_plans_src = f"{base_dir}/lesson_plans"
    support_material_src = f"{base_dir}/support_material"
    lesson_plans_dst = f"{tefltools_dir}/lesson_plans/{course_name}"
    os.makedirs(lesson_plans_dst, exist_ok=True)
    for item in os.listdir(lesson_plans_src):
        shutil.move(os.path.join(lesson_plans_src, item), lesson_plans_dst)
    if os.path.exists(support_material_src):
        for item in os.listdir(support_material_src):
            shutil.move(os.path.join(support_material_src, item), lesson_plans_dst)
    print(f"Moved lesson plans and support material to {lesson_plans_dst}")

    # Move Readings, activities, and quizzes
    for folder in ['Readings', 'activities', 'quizzes']:
        src_folder = f"{base_dir}/{folder}"
        dst_folder = f"{tefltools_dir}/{folder}/{course_name}"
        os.makedirs(dst_folder, exist_ok=True)
        for item in os.listdir(src_folder):
            shutil.move(os.path.join(src_folder, item), dst_folder)
        print(f"Moved {folder} to {dst_folder}")

def analyze_all_content(content_folder):
    """Analyze all PDF content and determine an inclusive course topic."""
    all_content = ""
    for filename in os.listdir(content_folder):
        if filename.lower().endswith('.pdf'):
            print(f"Reading: {filename}")
            file_path = os.path.join(content_folder, filename)
            all_content += read_file_content(file_path) + "\n\n"
            print(f"Read content from: {file_path}")

    prompt = f"""Analyze the following content from multiple PDF files and provide a summary of the main topics and themes. This will be used to generate a course syllabus, so focus on identifying overarching themes and key areas of study:

{all_content[:50000]}  # Limit to first 50000 characters to fit within token limits

Based on this content, suggest an inclusive course topic that encompasses the major themes found in all the documents. Your response should be structured as follows:

1. Main Course Topic: [Suggested course topic]
2. Key Themes:
   - [Theme 1]
   - [Theme 2]
   - [Theme 3]
   ...
3. Brief Overview: [2-3 sentences summarizing the content and its relevance to the course topic]
"""

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0.2,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def generate_syllabus(course_topic, truncated_info):
    """Generate a syllabus based on the analyzed course topic and project information using Claude."""
    prompt = f"""Given the following course topic and key themes:
{course_topic}

And the following additional project information:
{truncated_info}

Please do the following:
1. Create a well-structured syllabus for a program based on the provided course topic and themes.
2. Localize the content for Timor Leste, considering cultural context and appropriateness.
3. Include in the syllabus:
   - Course title (based on the main course topic)
   - Course overview and objectives
   - A structure that includes a sequence of 6-8 learning units
   - For each learning unit, provide:
     * Clear objectives
     * Topics to be covered
     * Activities or assignments
   - Required resources (books, materials)
   - Suggested items to cover
   - Ideas for practical experience and community engagement
   - Additional resources

Format the output as Markdown, with clear headings and subheadings for each section. Use the following structure:

# [Course Title]

## Course Overview and Objectives

[Course overview and objectives here]

## Learning Unit 1: [Unit Title]
- Objectives:
  * [Objective 1]
  * [Objective 2]
- Topics:
  * [Topic 1]
  * [Topic 2]
- Activities:
  * [Activity 1]
  * [Activity 2]

[Continue with more learning units]

## Required Resources

[List resources here]

## Suggested Items to Cover

[List suggested items here]

## Practical Experience and Community Engagement

[List ideas here]

## Additional Resources

[List additional resources here]

Ensure that each learning unit is clearly labeled and structured as shown above.
Don't add any commentary at the top, like 'Here is a syllabus...'"""

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
    time.sleep(2)  # Pause for 2 seconds after Anthropic call
    return message.content[0].text if message.content else ""

def main():
    course_name = input("Enter the name of the course: ")
    cleaned_course_name = clean_name(course_name)

    base_dir = f"courses/{cleaned_course_name}"
    create_directory(f"{base_dir}/syllabus")
    create_directory(f"{base_dir}/lesson_plans")
    create_directory(f"{base_dir}/Readings")
    create_directory(f"{base_dir}/activities")
    create_directory(f"{base_dir}/quizzes")
    create_directory(f"{base_dir}/support_material")

    syllabus_filename = f'{cleaned_course_name}.md'
    syllabus_path = f'{base_dir}/syllabus/{syllabus_filename}'
    content_folder = 'content'
    
    if os.path.exists(syllabus_path):
        print(f"Loading existing syllabus from {syllabus_path}")
        with open(syllabus_path, 'r', encoding='utf-8') as file:
            syllabus = file.read()
        course_topic = "Existing course topic"  # Placeholder for existing courses
    else:
        print("Analyzing all content files...")
        course_topic = analyze_all_content(content_folder)
        print("Course topic analysis complete.")
        
        print("Generating syllabus...")
        project_info = ""
        for filename in os.listdir(content_folder):
            if filename.lower().endswith(('.pdf', '.txt', '.md', '.docx')):
                file_path = os.path.join(content_folder, filename)
                project_info += read_file_content(file_path) + "\n\n"
        
        print(f"Total content size before truncation: {len(project_info)} characters")
        truncated_info = truncate_to_token_limit(project_info, max_tokens=170000)
        print(f"Truncated content size: {len(truncated_info)} characters")
        
        syllabus = generate_syllabus(course_topic, truncated_info)
        write_to_file(syllabus, syllabus_path)
        print("Syllabus generation complete.")
    
    print("Syllabus content:")
    print(syllabus[:500])  # Print first 500 characters
    learning_units = extract_learning_units(syllabus)
    print(f"Extracted {len(learning_units)} learning units")

    lesson_plans = []
    for i, unit in enumerate(learning_units, 1):
        lesson_plan_path = f"{base_dir}/lesson_plans/Unit_{i}_Lesson_Plan.md"
        if os.path.exists(lesson_plan_path):
            print(f"Loading existing lesson plan for Unit {i}")
            with open(lesson_plan_path, 'r', encoding='utf-8') as file:
                lesson_plan = file.read()
        else:
            try:
                lesson_plan = generate_lesson_plan(unit, syllabus, truncated_info)
                write_to_file(lesson_plan, lesson_plan_path)
                print(f"Generated and wrote lesson plan for Unit {i}")
            except Exception as e:
                print(f"Error generating lesson plan for Unit {i}: {str(e)}")
                continue
        
        lesson_plans.append(lesson_plan)
        
        # Generate and write activities
        activities_path = f"{base_dir}/activities/Unit_{i}_Activities.md"
        if not os.path.exists(activities_path):
            try:
                activities = generate_activities(lesson_plan, syllabus)
                write_to_file(activities, activities_path)
            except Exception as e:
                print(f"Error generating activities for Unit {i}: {str(e)}")
        
        # Generate and write support material
        support_material_path = f"{base_dir}/support_material/Unit_{i}_Support_Material.md"
        if not os.path.exists(support_material_path):
            try:
                support_material = generate_support_material(lesson_plan, syllabus)
                write_to_file(support_material, support_material_path)
            except Exception as e:
                print(f"Error generating support material for Unit {i}: {str(e)}")
                print(f"Current working directory: {os.getcwd()}")
                print(f"Does the directory exist? {os.path.exists(os.path.dirname(support_material_path))}")

    for i, unit in enumerate(learning_units, 1):
        resources_path = f"{base_dir}/lesson_plans/Unit_{i}_Resources.md"
        if not os.path.exists(resources_path):
            try:
                resources = generate_lesson_resources(unit, syllabus, lesson_plans[i-1])
                content = f"# {unit.split(':')[0].strip()}\n\n{unit}\n\n## Unit Resources\n\n{resources}"
                write_to_file(content, resources_path)
            except Exception as e:
                print(f"Error generating resources for Unit {i}: {str(e)}")

    for i, unit in enumerate(learning_units, 1):
        unit_name = f"Unit {i}"
        additional_resources_section = re.search(r'## Additional Resources\s*([\s\S]*?)(?=\n#|$)', unit)
        if additional_resources_section:
            resources = re.findall(r'- (.+)', additional_resources_section.group(1))
            for resource in resources:
                try:
                    if resource.startswith('[') and '](' in resource and resource.endswith(')'):
                        link_text, url = re.match(r'\[(.*?)\]\((.*?)\)', resource).groups()
                        output_filename = f"{base_dir}/Readings/{clean_name(unit_name)}_{clean_name(link_text)}.txt"
                        if not os.path.exists(output_filename):
                            cleaned_content = fetch_and_clean_url_content(url)
                            if cleaned_content:
                                write_to_file(cleaned_content, output_filename)
                    else:
                        key = '_'.join(resource.split()[:3]).lower()
                        output_filename = f"{base_dir}/Readings/{clean_name(unit_name)}_additional_{clean_name(key)}.md"
                        if not os.path.exists(output_filename):
                            processed_content = process_additional_resource(unit_name, resource, syllabus, lesson_plans[i-1])
                            if processed_content:
                                write_to_file(processed_content, output_filename)
                except Exception as e:
                    print(f"Error processing additional resource in {unit_name}: {str(e)}")

    for i, lesson_plan in enumerate(lesson_plans, 1):
        reading_path = f"{base_dir}/Readings/Unit_{i}_Reading.md"
        if not os.path.exists(reading_path):
            try:
                reading = generate_reading(lesson_plan, syllabus, lesson_plans[i-1], truncated_info)
                write_to_file(reading, reading_path)
                print(f"Generated reading for Unit {i}")
            except Exception as e:
                print(f"Error generating reading for Unit {i}: {str(e)}")

    for i, unit in enumerate(learning_units, 1):
        quiz_path = f"{base_dir}/quizzes/Unit_{i}_Quiz.json"
        if not os.path.exists(quiz_path):
            try:
                context_files = {
                    f"{base_dir}/syllabus/{syllabus_filename}": syllabus,
                    f"{base_dir}/lesson_plans/Unit_{i}_Lesson_Plan.md": lesson_plans[i-1] if i <= len(lesson_plans) else "No lesson plan available",
                    f"{base_dir}/lesson_plans/Unit_{i}_Resources.md": open(f"{base_dir}/lesson_plans/Unit_{i}_Resources.md", 'r').read() if os.path.exists(f"{base_dir}/lesson_plans/Unit_{i}_Resources.md") else "No resources available",
                    f"{base_dir}/Readings/Unit_{i}_Reading.md": open(f"{base_dir}/Readings/Unit_{i}_Reading.md", 'r').read() if os.path.exists(f"{base_dir}/Readings/Unit_{i}_Reading.md") else "No reading available"
                }
                quiz_json = generate_quiz(unit, context_files, truncated_info)
                if quiz_json:
                    write_to_file(quiz_json, quiz_path)
                    print(f"Successfully generated and wrote quiz for Unit {i}")
                else:
                    print(f"Failed to generate quiz for Unit {i}: Empty response from API")
            except Exception as e:
                print(f"Error generating quiz for Unit {i}: {str(e)}")

    print(f"Course generation for '{course_name}' completed successfully.")
    print(f"Number of learning units: {len(learning_units)}")
    print(f"Generated {len(lesson_plans)} lesson plans.")
    print(f"Generated {len(os.listdir(f'{base_dir}/activities'))} activity files.")
    print(f"Generated {len(os.listdir(f'{base_dir}/support_material'))} support material files.")
    print(f"Generated {len(os.listdir(f'{base_dir}/Readings'))} reading files.")
    print(f"Generated {len(os.listdir(f'{base_dir}/quizzes'))} quiz files.")

    # Verification
    if len(os.listdir(f'{base_dir}/Readings')) != len(learning_units):
        print(f"Warning: Number of reading files ({len(os.listdir(f'{base_dir}/Readings'))}) does not match number of learning units ({len(learning_units)})")

    # Move files to TEFLTools repository structure
    move_files_to_tefltools(base_dir, cleaned_course_name)
    print("Files have been moved to the TEFLTools repository structure.")

if __name__ == "__main__":
    main()