import cv2
import numpy as np

imagen = cv2.imread('lunares.png')
imgHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

#se definen los rangos de los colores para su deteccion 
amarilloBajo = np.array([20,100,20], np.uint8)
amarilloAlto = np.array([32,255,255], np.uint8)
maskAmarillo = cv2.inRange(imgHSV,amarilloBajo,amarilloAlto)

violetaBajo = np.array([130,100,20], np.uint8)
violetaAlto = np.array([145,255,255], np.uint8)
maskVioleta = cv2.inRange(imgHSV,violetaBajo,violetaAlto)

verdeBajo = np.array([36,100,20], np.uint8)
verdeAlto = np.array([70,255,255],np.uint8)
maskVerde = cv2.inRange(imgHSV,verdeBajo, verdeAlto)


cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
