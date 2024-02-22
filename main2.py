
#setup
import bob
import pytesseract
import easyocr
from PIL import Image

#to take picture
import pic

'''img = cv2.imread("Photos\mo.png")
reader = easyocr.Reader(['en'], gpu = False)
text = reader.readtext(img, detail = 1)
print(text)
'''
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path = 'model_write.png'
# Open the image using PIL (Python Imaging Library)
img = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text.replace(' ',""))
