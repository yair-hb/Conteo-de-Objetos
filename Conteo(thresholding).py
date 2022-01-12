import cv2

#se lee la imagen de entrada 
imagen = cv2.imread('monedas.jpg')

#se transforma la imagen de bgr a gris para trabajar en ella
imgris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

#aplicamos la umbralizaion invertida ya wue el fondo de la imagen es blanco
_,th = cv2.threshold(imgris,240,255, cv2.THRESH_BINARY_INV)

#se buscan los contornos que seran las referencias
contornos,_ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# se dibujan los contornos de las imagenes encontradas
cv2.drawContours(imagen, contornos, -1, (0,0,255),2)
print ('Contornos:', len(contornos))

font = cv2.FONT_HERSHEY_SIMPLEX
i=0
for c in contornos:
    M = cv2.moments(c)
    if (M["m00"]==0): M["m00"]=1
    x= int(M["m10"]/M["m00"])
    y= int(M["m01"]/M["m00"])

    mensaje = 'Num: ' + str(i+1)
    cv2.putText(imagen,mensaje,(x-40,y),font,0.75,(255,0,0),2,cv2.LINE_AA)
    cv2.drawContours(imagen, [c],0,(255,0,0),2)

    cv2.imshow('IMAGEN DE ENTRADA', imagen)
    cv2.imshow('IMAGEN GRAY',imgris)
    cv2.waitKey(0)
    i = i+1
cv2.destroyAllWindows()
