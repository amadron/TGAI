# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import arange
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
    
mean = []
x = []

for num in range(10,73,3):
    print('range:'+str(num)+'cm')
    val=np.genfromtxt(str(num) + 'cm.csv',delimiter=',',usecols=(4,4))
    print('mean: '+ str(np.mean(val)) + 'V')
    mean.append(np.mean(val))
    lnval = np.log(mean)
    dev = np.std(val)
    print('devation:'+str(dev)+'V'+'\n')

    
    #lineare regression 
x = arange(10,73,3)
slope, intercept, r_value, p_value, std_err  = stats.linregress(x, lnval)
line = slope*x+intercept
finalf = np.exp(slope*(x)+intercept)

    #Fehlerberechnung
width=np.genfromtxt('width.csv',delimiter=',',usecols=(4,4))
length=np.genfromtxt('length.csv',delimiter=',',usecols=(4,4))

mwidth=np.mean(width)
mlength=np.mean(length)

stdwidth=np.std(width)
stdlength=np.std(length)

dwidth95=stdwidth*1.96
dlength95=stdlength*1.96

fwidth=((np.log(mwidth)/slope)-intercept/slope)
fdwidth68=(stdwidth/mwidth)*fwidth
fdwidth95=(dwidth95/mwidth)*fwidth

flength=((np.log(mlength)/slope)-intercept/slope)
fdlength68=(stdlength/mlength)*flength
fdlength95=(dlength95/mlength)*flength


print('length:'+'\n''voltage'+str(mlength)+'V\n'+'deltaV 68%(+-):'+
str(stdlength)+'V\n' +'deltaV 95%(+-):'+str(dlength95)+'V\n''length:'+str(flength)+'cm \n'
+'delta_length 68%(+-):' +str(fdlength68)+'cm \n'+'delta_length 95%(+-):'+str(fdlength95)+'cm \n')

print('width:'+'\n''voltage'+str(mwidth)+'V\n'+'deltaV 68%(+-):'+
str(stdwidth)+'V\n' +'deltaV 95%(+-):'+str(dwidth95)+'V\n''width:'+str(fwidth)+'cm \n'
+'delta_width 68%(+-):' +str(fdwidth68)+'cm \n'+'delta_width 95%(+-):'+str(fdwidth95)+'cm \n')

    #Flaechenberechnung
area=flength*fwidth
area68=np.sqrt((flength*fdwidth68)**2+(fwidth*fdlength68)**2)
area95=np.sqrt((flength*fdwidth95)**2+(fwidth*fdlength95)**2)
print('Area:'+str(area)+'cm^2')
print('delta 68%(+-):'+str(area68)+'cm^2')
print('delta 95%(+-):'+str(area95)+'cm^2')





    #plotting commands
#plt.plot(val)
#plt.plot(mean,x,'o',mean,x,'r-')
#plt.plot(lnval,x,'o',line,x,'r-')
#plt.plot(finalf,x)
#plt.plot(finalf,x,'r-',mean,x,'o')

