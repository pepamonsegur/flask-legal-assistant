from cloudmersive_convert_api_client import ConvertDocumentApi
from cloudmersive_convert_api_client.rest import ApiException
import pytesseract
from PIL import Image
import io

# Function to extract text from PDF using Cloudmersive
def extract_text_from_pdf(file):
    try:
        # Debug: Log file metadata
        print(f"File name: {file.filename}")
        print(f"File type: {file.content_type}")

        # Read the file content
        file_content = file.read()

        # Check for null bytes in the content
        if b'\x00' in file_content:
            raise ValueError("The uploaded file contains embedded null bytes")

        # Use the Cloudmersive API or another OCR process
        print("File content read successfully. Proceeding with Cloudmersive API.")
        # Call your Cloudmersive conversion function here (as defined previously)
        # Replace this with the Cloudmersive API call to convert PDF to images
        return "Processed text from the PDF."

    except Exception as e:
        print(f"Error processing the file: {e}")
        return "Error processing the file. Please check the file and try again."
