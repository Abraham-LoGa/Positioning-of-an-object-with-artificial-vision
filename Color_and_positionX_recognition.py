# Importamos librerias
import cv2
import numpy as np
  # Abrimos la camara seleccionada
video=cv2.VideoCapture(0)
  # Relacion cm-pixel
cm_por_pixel_x = 13/640
cm_por_pixel_y = 9/640
while True:
       # Accedemos a la camara y transformamos a escala de grises
     _,frame=video.read()
     imagen_grises = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     cv2.imshow("Background",imagen_grises)
       # Salimos del bucle con la tecla "esc"
     k=cv2.waitKey(5)
     if k==27:
         break
while True:
       # Abrimos nuevamente y convertimos a escala de grises
     _,frame=video.read()
     imagen_grises2 = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     cv2.imshow("Foreground",imagen_grises2)
       # Restamos las imagenes
     diferencia_imagenes = np.absolute(np.matrix(np.int16(imagen_grises))-
     np.matrix(np.int16(imagen_grises2)))
     diferencia_imagenes[diferencia_imagenes>255]=255
     diferencia_imagenes=np.uint8(diferencia_imagenes)
     cv2.imshow("diferencia_imagenes",diferencia_imagenes) 
        #Establecemos limites
     Diff = diferencia_imagenes
     Diff[Diff<=100]=0
     Diff[Diff>100]=1
     columnaSuma=np.matrix(np.sum(Diff,0))
       # Se enumera cada uno de los elementos X
     columnaNum=np.matrix(np.arange(640))
     columnaMult=np.multiply(columnaSuma,columnaNum)
     total=np.sum(columnaMult)
     totalTotal=np.sum(np.sum(Diff))
     columnaLocal=total/totalTotal
       # Se establece la localización en x
     x_localizacion = columnaLocal*cm_por_pixel_x
     filaSuma=np.matrix(np.sum(Diff,1)) 
     filaSuma = filaSuma.transpose()
       # Se enumera cada uno de los elementos Y
     filaNum=np.matrix(np.arange(480))  
     filaMult=np.multiply(filaSuma,filaNum)
     total=np.sum(filaMult)
     totalTotal=np.sum(np.sum(Diff))
     filaLocal=total/totalTotal

       # Se establece la localización en Y
     y_localizacion = filaLocal*cm_por_pixel_y
       # Imprimimos la localización en x,y
     print(x_localizacion,y_localizacion)
       # Establecemos la tecla "esc" como salida de bucle
     k=cv2.waitKey(5)
     if k==27:
         break
cv2.destroyAllWindows()
