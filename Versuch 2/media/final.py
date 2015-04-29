# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:09:26 2015

@author: Kuba
"""

import numpy as np
import cv2

gbild = cv2.imread('graubild.png')
dbild = cv2.imread('Dunkelbild.png')
wbild = cv2.imread('Weissbild.png')

final = gbild - dbild
korrektur = float(np.mean(wbild))
nwbild = wbild / korrektur
final = final/nwbild

cv2.imshow('show', final)
cv2.waitKey()

#cv2.imwrite('finalgrau.png', final)
