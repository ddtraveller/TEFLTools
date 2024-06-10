import io
from PyPDF2 import PdfReader
import pandas as pd

if __name__ == '__main__':
    # Specify the path to your PDF file
    pdf_path = '/home/ubuntu/environment/FedEx.pdf'

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

    # Save the DataFrame to a CSV file
    output_path = '/home/ubuntu/environment/extracted_text.csv'
    df.to_csv(output_path, index=False)

    print(f"Extracted text saved to: {output_path}")