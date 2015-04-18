import numpy as np

data = np.genfromtxt("10cm.csv", skip_header=17,delimiter=',', usecols=(3,4,9,10))
print(data)