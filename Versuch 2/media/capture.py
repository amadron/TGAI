# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 14:13:06 2015

@author: dakubatz
"""

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        for nr in range (0,10):
            cv2.imwrite('wbild' + str(nr) +'.png', frame)
        break;
cap.release()
cv2.destroyAllWindows()
