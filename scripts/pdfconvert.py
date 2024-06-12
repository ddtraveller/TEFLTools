import io
from PyPDF2 import PdfReader
import pandas as pd

if __name__ == '__main__':
    # Prompt the user to enter the PDF file path
    pdf_path = input("Enter the path to your PDF file: ")
    # pdf_path = '/home/ubuntu/environment/FedEx.pdf'
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PdfReader(file)
            # Initialize a list to store the extracted text
            extracted_text = []
            # Iterate over each page of the PDF
            for page in pdf_reader.pages:
                # Extract the text from the page
                text = page.extract_text()
                # Split the text into lines
                lines = text.split('\n')
                # Append each line as a separate element in the list
                extracted_text.extend(lines)

        # Create a DataFrame from the extracted text
        df = pd.DataFrame(extracted_text, columns=['Text'])

        # Prompt the user to enter the output file path
        output_path = input("Enter the path to save the extracted text (e.g., /path/to/extracted_text.csv): ")

        # Save the DataFrame to a CSV file
        df.to_csv(output_path, index=False)
        print(f"Extracted text saved to: {output_path}")

    except FileNotFoundError:
        print("The specified PDF file path does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
