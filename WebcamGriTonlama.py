import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # gri tonlama yapmamızı saglar.
    cv2.imshow('frame',frame)  # normal webcam framelerimiz.
    cv2.imshow('gray',gray)  #ikinci bir gri tonlamalı gray frame olusturur.
    


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
