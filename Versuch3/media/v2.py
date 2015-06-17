# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:47:30 2015

@author: dakubatz
"""

import numpy as np
import matplotlib.pyplot as plt
pg1 = []
pg2 = []

freq=[100,200,300,400,500,700,850,1000,1200,
      1500,1700,2000,3000,4000,5000,6000,10000]
amp1=[27.2,80,52,38.4,29.6,22.4,25.6,27.2,23.6,
     21.6,23.2,31.6,21.6,27.6,19.6,18.4,17.2] 
ph1=[4.5,4.4,3.49,2.78,2.3,1.66,1.35,1.21,1.02,
    0.86,0.77,0.67,0.47,0.34,0.24,0.19,0.16]
    
amp2=[3.36,9.68,16.6,32.2,66.8,30.4,26.8,24.4,
      20.4,18.8,17.6,19.2,21,7.2,18.6,2.8,7.2,]
ph2=[3.4,2.64,2.32,1.84,2.12,1.65,1.33,1.18,1.03,
     0.85,0.79,0.68,0.49,0.41,0.37,0.29,0.15]  
     
for i in range (0,17):
    pg1.append(-1*ph1[i]/1000*freq[i]*360)
    pg2.append(-1*ph2[i]/1000*freq[i]*360)     

fig, ax = plt.subplots(figsize=(800/100, 600/100), dpi=100)
ax.semilogx(freq,20*np.log10(amp1))
ax.set_xlabel('Kreisfrequenz')
ax.set_ylabel('Amplitudengang[$dB$]')
ax.set_title('Amplitudengang: großer Lautsprecher')

fig, ax = plt.subplots(figsize=(800/100, 600/100), dpi=100)
ax.semilogx(freq,pg1)
ax.set_xlabel('Kreisfrequenz')
ax.set_ylabel('Phasenwinkel[$Grad$]')
ax.set_title('Phasengang: großer Lautsprecher')

fig, ax = plt.subplots(figsize=(800/100, 600/100), dpi=100)
ax.semilogx(freq,20*np.log10(amp2))
ax.set_xlabel('Kreisfrequenz')
ax.set_ylabel('Amplitudengang[$dB$]')
ax.set_title('Amplitudengang: kleiner Lautsprecher')

fig, ax = plt.subplots(figsize=(800/100, 600/100), dpi=100)
ax.semilogx(freq,pg2)
ax.set_xlabel('Kreisfrequenz')
ax.set_ylabel('Phasenwinkel[$Grad$]')
ax.set_title('Phasengang: kleiner Lautsprecher')




     