import cv2
import numpy as np

#se dibuja los contornos y se enumeran cada uno de los circulos encontrados 
def dibujarContorno (contornos, color):
    for (i,c) in enumerate(contornos):
        M = cv2.moments(c)
        if (M["m00"]==0): M["m00"]==1
        x = int (M["m10"]/M["m00"])
        y = int (M["m01"]/M["m00"])
        cv2.drawContours(imagen,[c],0, color,2)
        cv2.putText(imagen,str(i+1),(x-10,y+10),1,2,(0,0,0),2)

#se definen los rangos de los colores para su deteccion 
amarilloBajo = np.array([20,100,20], np.uint8)
amarilloAlto = np.array([32,255,255], np.uint8)

violetaBajo = np.array([130,100,20], np.uint8)
violetaAlto = np.array([145,255,255], np.uint8)

verdeBajo = np.array([36,100,20], np.uint8)
verdeAlto = np.array([70,255,255],np.uint8)

rojoBajo1 = np.array([0,100,20],np.uint8)
rojoAlto1 = np.array([10,255,255],np.uint8)
rojoBajo2 = np.array([175,100,20],np.uint8)
rojoAlto2 = np.array([180,255,255],np.uint8)

#se declaran las variables de las imagenes a tratar
imagen = cv2.imread('lunares.png')
imgHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

#se detectan los colores de la imagen
maskAmarillo = cv2.inRange(imgHSV,amarilloBajo,amarilloAlto)
maskVioleta = cv2.inRange(imgHSV,violetaBajo,violetaAlto)
maskVerde = cv2.inRange(imgHSV,verdeBajo, verdeAlto)
maskRojo1 = cv2.inRange(imgHSV,rojoBajo1,rojoAlto1)
maskRojo2 = cv2.inRange(imgHSV,rojoBajo2,rojoAlto2)
maskRojo = cv2.add(maskRojo1,maskRojo2)

#se encuentran los contornos de cada uno de los colores 
cntsAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cntsVioleta = cv2.findContours(maskVioleta,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cntsVerde = cv2.findContours(maskVerde,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cntsRojo = cv2.findContours(maskRojo,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

dibujarContorno(cntsAmarillo, (0, 255,255))
dibujarContorno(cntsVioleta, (140, 40, 120))
dibujarContorno(cntsVerde, (0, 255, 0))
dibujarContorno(cntsRojo, (0, 0, 255))

imgResumen = 255 * np.ones((210,100,3), dtype = np.uint8)
cv2.circle(imgResumen, (30,30), 15, (0,255,255), -1)
cv2.circle(imgResumen, (30,70), 15, (140,40,120), -1)
cv2.circle(imgResumen, (30,110), 15, (0,255,0), -1)
cv2.circle(imgResumen, (30,150), 15, (0,0,255), -1)
cv2.putText(imgResumen,str(len(cntsAmarillo)),(65,40), 1, 2,(0,0,0),2)
cv2.putText(imgResumen,str(len(cntsVioleta)),(65,80), 1, 2,(0,0,0),2)
cv2.putText(imgResumen,str(len(cntsVerde)),(65,120), 1, 2,(0,0,0),2)
cv2.putText(imgResumen,str(len(cntsRojo)),(65,160), 1, 2,(0,0,0),2)
totalCnts = len(cntsAmarillo) + len(cntsVioleta) + len(cntsVerde) + len(cntsRojo)
cv2.putText(imgResumen,str(totalCnts),(55,200), 1, 2,(0,0,0),2)
cv2.imshow('Resumen', imgResumen)


#cv2.imshow('AMARILLO', maskAmarillo)
#cv2.imshow('VIOLETA', maskVioleta)
#cv2.imshow('VERDE', maskVerde)
#cv2.imshow('ROJO', maskRojo)
cv2.imshow('IMAGEN', imagen)
#cv2.imwrite('conteo.png', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
