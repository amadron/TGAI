# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 13:59:13 2015

@author: dakubatz
"""

import numpy as np
import matplotlib.pyplot as plt
import redlab as rl
import time

def AdcRead():
    return np.median(rl.cbVInScan(0,0,0,4000,8000,1))

def AdcScan():
    return rl.cbVInScan(0,0,0,4000,8000,1)
    
def DAOut(v):
    return rl.cbVOut(0,0,101,v)    

def sinus():
    samples = 10
    t = np.linspace(0, 2*np.pi, samples)
    y = np.sin(t)
    y = y + np.abs(np.min(y))
    for i in y:
        DAOut(i)
        time.sleep(1/samples)
        
def nyquist():
    freq = np.linspace(2000,8000,7)
    x = np.linspace(0,4000/8000, 4000)
    dt=1/8000
    for i in freq:
        print(i)
        input()
        y = AdcScan()
        plot(x,y, 'Zeit [$s$]', 'Amplitude [$V$]', '$f={0}$, $f_s={1}$'.format(int(i), 8000), '{0}-signal.png'.format(i))
        spec=np.abs(np.fft.fft(y)/len(y))
        fftLen = len(spec)
        f=np.zeros(fftLen)
        for j in range(0,fftLen):
            f[j]=j/(fftLen*dt)
        plot(f, spec,'frequency [$f$]', '$|Y(f)|$', '$f={0}$, $f_s={1}$'.format(int(i), 8000), '{0}-fft.png'.format(i))

def plot(x,y, xLabel, yLabel, title, filename):
    dpi = 75
    fig,ax = plt.subplots(figsize=(800/dpi,600/dpi), dpi=dpi)
    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    plt.show()
    fig.savefig(filename, transparent=True, pad_inches=0, dpi=75)