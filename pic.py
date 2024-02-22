import cv2
import time
import numpy as np
from PIL import Image, ImageFilter
import imutils
def take_pic():
    cam = cv2.VideoCapture(1)
    result, image = cam.read()
    time.sleep(1)
    result, image = cam.read()
    cv2.imwrite("model_write.png", image)
def show(x= "model_write.png"):
    if str(x) == "model_write.png":
        image = cv2.imread(x)
        cv2.imshow("Captured Image", image)
    else:
        cv2.imshow("Captured Image", x)
    cv2.waitKey(0)  # Wait for any key press
    cv2.destroyAllWindows()
def crop():
    # Read input image
    img = cv2.imread('model_write.png')

    # Convert from BGR to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Get the saturation plane - all black/white/gray pixels are zero, and colored pixels are above zero.
    s = hsv[:, :, 1]

    cv2.imwrite('s.png', s)

    # Apply threshold on s - use automatic threshold algorithm (use THRESH_OTSU).
    ret, thresh = cv2.threshold(s, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Find contours
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnts = imutils.grab_contours(cnts) 

    # Find the contour with the maximum area.
    c = max(cnts, key=cv2.contourArea)

    # Get bounding rectangle
    x, y, w, h = cv2.boundingRect(c)

    # Crop the bounding rectangle out of img
    out = img[y:y+h, x:x+w, :].copy()
    show(out)
#take_pic()    
show()
crop()