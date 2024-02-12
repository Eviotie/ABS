
#setup
import cv2
import bob
import pytesseract
import easyocr
try:
    from PIL import Image
except ImportError:
    import Image

cam = cv2.VideoCapture(0)
 
result, image = cam.read()
cv2.imwrite("model_write.png", cv2.flip(image, -1))
'''img = cv2.imread("Photos\mo.png")
reader = easyocr.Reader(['en'], gpu = False)
text = reader.readtext(img, detail = 1)
print(text)
'''
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path ="model_write.png"
image = Image.open(image_path)
text = pytesseract.image_to_string(image)
print(text)
