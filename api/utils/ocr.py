import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image

def extract_text_from_pdf(file):
    # Convierte PDF en imágenes
    images = convert_from_bytes(file.read())
    full_text = ""
    for image in images:
        full_text += pytesseract.image_to_string(image, lang='spa')
    return full_text
