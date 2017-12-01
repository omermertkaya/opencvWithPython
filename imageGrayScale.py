import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("watch.jpg",cv2.IMREAD_GRAYSCALE) # resmi gri tonlamadan gecir.
cv2.imshow('image',img) #resimi ekrana bas
cv2.waitKey(0)
cv2.destroyAllWindows()


#image jpg dosyanızı ismini degistirebilirsiniz.
#image dosyanız python projeniz ile aynı dizinde kayıtlı olmalıdır.
#yukarıda bu sekilde kodlanmıştır.
#omermertkaya
