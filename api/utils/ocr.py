from cloudmersive_convert_api_client import ConvertDocumentApi
from cloudmersive_convert_api_client.rest import ApiException
import pytesseract
from PIL import Image
import io

# Function to extract text from PDF using Cloudmersive
def extract_text_from_pdf(file):
    # Configure the Cloudmersive API client
    import cloudmersive_convert_api_client
    configuration = cloudmersive_convert_api_client.Configuration()
    configuration.api_key['Apikey'] = '4547e203-3095-4d96-9ec7-d0eb76399af4'  # Replace with your API key

    # Create an instance of the ConvertDocument API
    api_instance = ConvertDocumentApi(cloudmersive_convert_api_client.ApiClient(configuration))

    try:
        # Convert the PDF to JPG images
        result = api_instance.convert_document_pdf_to_jpg(file.read())

        # Process each image for OCR
        full_text = ""
        for image_data in result:
            image = Image.open(io.BytesIO(image_data))
            full_text += pytesseract.image_to_string(image, lang='spa')

        return full_text

    except ApiException as e:
        print("Exception when calling Cloudmersive API: %s\n" % e)
        return "Error processing the PDF"
