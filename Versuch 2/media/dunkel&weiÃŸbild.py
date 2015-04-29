# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 16:33:43 2015

@author: Kuba
"""

import numpy as np
import cv2
dbild = np.zeros((480,640))
wbild = np.zeros((480,640))

#dunkelbild
for nr in range (0,10):
    img = cv2.imread('dbild' + str(nr) +'.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(float)
    dbild = dbild + img
dbild = dbild/10    

#weissbild:
for nr in range (0,10):
    img = cv2.imread('wbild' + str(nr) +'.png')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    wbild = wbild + img
wbild = wbild/10

wbild = wbild - dbild   

#kontrast maximierung
dbildcontrast = dbild*100
wbildcontrast = wbild*100
  
#cv2.imshow('show', wbildcontrast)
#cv2.waitKey()

#cv2.imwrite('Dunkelbild.png', dbild)
#cv2.imwrite('Weissbild.png', wbild)
#cv2.imwrite('MaxDunkelbild.png', dbildcontrast)
