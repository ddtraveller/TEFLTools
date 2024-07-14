import os
import anthropic
import PyPDF2
import warnings

# Load API key from environment variable
api_key = os.getenv('ANTHROPIC_API_KEY')
if not api_key:
    raise ValueError("Please set the ANTHROPIC_API_KEY environment variable")

client = anthropic.Anthropic(api_key=api_key)

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Suppress specific warnings
        warnings.filterwarnings("ignore", category=PyPDF2.errors.PdfReadWarning)
        for page in reader.pages:
            try:
                text += page.extract_text() + "\n"
            except Exception as e:
                print(f"Error extracting text from page: {e}")
                continue
    return text

def summarize_text(text):
    # Truncate text if it's too long
    max_chars = 100000  # Adjust this value based on API limits
    if len(text) > max_chars:
        text = text[:max_chars] + "..."

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system="You are an expert summarizer. Provide a concise summary of the given text.",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"Please summarize the following text:\n\n{text}"
                        }
                    ]
                }
            ]
        )
        return message.content
    except Exception as e:
        return f"Error generating summary: {e}"

# Example usage
pdf_path = "/home/ubuntu/environment/TEFLTools/An-Indigenous-Peoples-History-of-the-United-States-Ortiz.pdf"
pdf_text = extract_text_from_pdf(pdf_path)

if pdf_text.strip():
    summary = summarize_text(pdf_text)
    print("Summary of the PDF:")
    print(summary)
else:
    print("Failed to extract text from the PDF.")