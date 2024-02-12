#import Main
import cv2
from . import bob
cam = cv2.VideoCapture(0)
 
result, image = cam.read()
if result:
    
    # show the image
    cv2.imshow("GeeksForGeeks", image)
    cv2.waitKey(0) 
    cv2.destroyWindow("GeeksForGeeks") 
    
    # save the image
    #imwrite("GeeksForGeeks.png", image)

#else:
    #Move to this part is input image has some error