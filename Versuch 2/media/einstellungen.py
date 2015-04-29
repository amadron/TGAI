# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:49:10 2015

@author: dakubatz
"""

import cv2
cap = cv2.VideoCapture(0)
#cap.set(12,12)
print("frame width: " + str(cap.get(3)))
7
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))
cap.release()
