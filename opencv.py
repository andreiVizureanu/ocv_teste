
from email.mime import image
import cv2 as cv
import sys
import numpy as np
X_DIMENSION = 800
Y_DIMENSION = 600
black_image = np.zeros((X_DIMENSION,Y_DIMENSION,3), np.uint8)

img = cv.imread(cv.samples.findFile("c://STUFF/1.jpg"))
if img is None:
    sys.exit("Could not read the image.")
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
cv.circle(black_image, [10,10], 10, [214, 214, 4], -1)
cv.putText(black_image, " <- Culoare cautata", (20, 20), cv.FONT_HERSHEY_PLAIN, 1, (110,110, 110), 1)
cv.imshow("Display img", img)
cv.imshow("Display black_image", black_image)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("c://STUFF/starry_night.png", img)