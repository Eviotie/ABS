

import time
import cv2


cam = cv2.VideoCapture(1)
result, image = cam.read()
time.sleep(.7)
result, image = cam.read()
cv2.imwrite("model_write.png", image)

def show():
    cv2.imshow("Captured Image", image)
    cv2.waitKey(0)  # Wait for any key press
    cv2.destroyAllWindows()
    
    
show()