import cv2  # opencv import edilir
import numpy as np  # numpy import edilir

cap = cv2.VideoCapture(0) #bilgisayarin web kamerasından video dondurur

while True:   # bu while dongusu sayesinde ekran olusturulur
    ret, frame = cap.read() 

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  #ekranda q tusuna basıldığında sona erdirir.
        break

cap.release()
cv2.destroyAllWindows()


#.
#..
#...
#Pencere icersinde web kamerasindan aldıgımız goruntleri gosterme.
#...
#..
#.
#omermertkaya
