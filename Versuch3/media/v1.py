# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import TekTDS2000 as tds
import numpy as np
import matplotlib.pyplot as plt
scope = tds.TekTDS2000()

x,y=scope.getData(1)
#np.savetxt("v1.csv", np.asarray([x,y]).T, delimiter=",")

dt=scope.getSamplingInterval()
spec=np.abs(np.fft.fft(y))

f=np.zeros(len(spec))

for i in range(0,len(spec)):
    f[i]=i/(len(spec)*dt)


fig, ax = plt.subplots(figsize=(800/100, 600/100), dpi=100)
ax.plot(f[0:len(spec)/2],spec[0:len(spec)/2]/len(spec))
ax.set_xlabel('Frequency [$Hz$]')
ax.set_ylabel('$|Y(f)|$')
ax.set_title('Mundharmonika Spektrum $f_s$: '+str(np.ceil(1/dt)))
plt.savefig('v1_fft.png', dpi=100)

print('Grundfrequenz: '+str(np.argmax(spec[0:len(spec)/2])/(len(spec)*dt)))

amp = spec[np.argmax(spec[0:len(spec)/2])]/len(spec)
print('Amplitude: ' +str(amp))
