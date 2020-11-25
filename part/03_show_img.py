#install opencv-python
#install numpy
'''
if you get message 'numpy.core.multiarray failed to import ...', check opencv-python version 4.4 and numpy version 1.19.3
if you have numpy version 1.19.4, you have to install specify version 1.19.3
'''
import cv2

img = cv2.imread('./capture.png')
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()