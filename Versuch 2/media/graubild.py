# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:56:33 2015

@author: dakubatz
"""

import numpy as np
import cv2
#img = cv2.imread('graubild.png')       #urspruengliches Bild
img = cv2.imread('finalgrau.png')       #bearbeitetes Bild
white=img[0:,0:90]
lgray=img[0:,135:225]
gray=img[0:,275:365]
dgray=img[0:,415:505]
black=img[0:,550:640]

mwhite=np.mean(white)
mlgray=np.mean(lgray)
mgray=np.mean(gray)
mdgray=np.mean(dgray)
mblack=np.mean(black)

print(mwhite)
print(mlgray)
print(mgray)
print(mdgray)
print(mblack)
print('\n')
print(np.std(white))
print(np.std(lgray))
print(np.std(gray))
print(np.std(dgray))
print(np.std(black))

#cv2.imshow('show', black)
#cv2.waitKey()