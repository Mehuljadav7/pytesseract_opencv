try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

image1 = Image.open("C:\python\program\image\imagetwo.jpg")

# Simple image to string
print(pytesseract.image_to_string(image1))