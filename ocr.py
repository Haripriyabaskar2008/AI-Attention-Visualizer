import pytesseract
from PIL import Image


def extract_text_from_image(image):
    """
    Extract text from an image using OCR.
    """

    text = pytesseract.image_to_string(image)

    return text.strip()


if __name__ == "__main__":

    print("OCR module loaded successfully.")
    print("Upload an image through the Streamlit application to extract text.")