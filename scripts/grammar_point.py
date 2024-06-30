import anthropic
import os
import re
import random

# This script will take a lesson plan and send it to anthropic along with a grammar point and update the lesson plan with
# grammar points that are relevant to the lesson in question.


GRAMMAR_POINTS = [
    "Tenses", "Modal Verbs", "Conditionals", "Passive Voice", "Questions and Negatives",
    "Reported Speech", "Nouns and Articles", "Pronouns", "Adjectives and Adverbs",
    "Prepositions", "Conjunctions", "Sentence Structure", "Punctuation", "Word Formation"
]

def list_files():
    return sorted([f for f in os.listdir('.') if f.endswith(('.txt', '.md'))])

def remove_existing_grammar_section(content):
    return re.sub(r'## Grammar Points:.*?(?=\n#|$)', '', content, flags=re.DOTALL).strip()

def update_grammar_section(file_path, grammar_emphasis):
    client = anthropic.Anthropic()
    
    with open(file_path, 'r') as file:
        lesson_content = file.read()
    
    lesson_content_without_grammar = remove_existing_grammar_section(lesson_content)
    
    grammar_prompt = f"""Given the following lesson plan content:

{lesson_content_without_grammar}

Generate a Grammar Points section for this specific lesson plan. 
Include 3-5 relevant grammar points that might be useful when discussing the concepts in this lesson.
Emphasize the use of {grammar_emphasis} in the context of this lesson.
Format the output as a Markdown list, starting with the title '## Grammar Points:' followed by the list items."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": grammar_prompt
            }
        ]
    )

    new_grammar_section = message.content[0].text if message.content else ""
    new_grammar_section = new_grammar_section.strip()

    updated_content = f"{lesson_content_without_grammar}\n\n{new_grammar_section}"

    with open(file_path, 'w') as file:
        file.write(updated_content)
    
    print(f"File '{file_path}' has been updated with new grammar points on {grammar_emphasis}.")

def main():
    files = list_files()
    if not files:
        print("No .txt or .md files found in the current directory.")
        return

    # Shuffle the grammar points list
    shuffled_grammar_points = GRAMMAR_POINTS.copy()
    random.shuffle(shuffled_grammar_points)
    print("Shuffled grammar points for this run:", ', '.join(shuffled_grammar_points))

    grammar_point_index = 0
    for file in files:
        grammar_point = shuffled_grammar_points[grammar_point_index]
        try:
            update_grammar_section(file, grammar_point)
        except Exception as e:
            print(f"Error processing {file} with {grammar_point}: {str(e)}")
        
        # Move to the next grammar point, wrapping around if necessary
        grammar_point_index = (grammar_point_index + 1) % len(shuffled_grammar_points)

if __name__ == "__main__":
    main()