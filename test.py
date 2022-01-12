import cv2

imagen = cv2.imread('monedas.jpg')
imgris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

bordes = cv2.Canny(imgris, 0,900)
contornos,_ = cv2.findContours(bordes,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen, contornos,-1,(0,0,255),2)

print ('Numero de contornos: ', len(contornos))
texto = 'Contornos encontrados: '+str(len(contornos))
cv2.putText(imagen, texto,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),1)

cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.imshow('IMAGEN CANNY', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()