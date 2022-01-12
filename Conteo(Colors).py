import cv2
import numpy as np

imagen = cv2.imread('lunares.png')

cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
