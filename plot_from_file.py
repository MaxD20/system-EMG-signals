#import pandas as pd
import time
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

x = []
y = []

with open('EMG_Data2.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        y.append(float(row[0]))
        #y.append(int(row[1]))
        x = np.linspace(0,5827,500)
        
peaks = find_peaks(y, height=1550, distance=20)
height = peaks[1]['peak_heights'] #list of the heights of the peaks
peak_pos = x[peaks[0]]

y2 = y*-1
minima = find_peaks(y2)
min_pos = x[minima[0]]
#min_height = y2[minima[0]]
#plt.plot(x, y, color = 'b', linestyle = 'dashed', label = "EMG Data")

print('Length of x is:',len(x))
print('Length of y is:',len(y))

'''
plt.plot(peaks, x[peaks], "x")
#plt.plot(np.zeros_like(x), "--", color="gray")
#plt.xticks(rotation = 25)
plt.xlabel('Time in Miliseconds')
plt.ylabel('MilliVolts')
plt.title('EMG Data', fontsize = 14)
plt.grid()
ax.grid()
plt.legend()
plt.show()'''

fig = plt.figure()
ax = fig.subplots()
ax.plot(x,y)
plt.title('EMG Data', fontsize=16)
plt.xlabel('Time in Milliseconds')
plt.ylabel('MilliVolts')
ax.scatter(peak_pos, height, color = 'r', s = 15, marker = 'D', label = 'Peeks from zygomaticus EMG')
ax.legend()
plt.grid()
ax.grid()
plt.legend()
plt.show()
