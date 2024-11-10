import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import find_peaks

import sys
import time
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

led_list = [17,18,27,22,23,24,21,10,25,9] # GPIO ports used

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Set all pins as output
for pin in led_list:
 GPIO.setup(pin,GPIO.OUT)

adc = Adafruit_ADS1x15.ADS1115(address = 0x48, busnum = 1)

GAIN = 1
scale = {2/3: 6.144,
         1 : 4.096,
         2 : 2.048,
         4 : 1.024,
         8 : 0.512,
         16 : 0.256}

x_len = 500
y_range = [0, 1900]


'''
x2 = np.arange(1,500,1)
y2 = 0.3 * np.sin(x2) + 0.7 * np.cos(2 * x2) - 0.5 * np.sin(1.2 * x2)
threshold = 1200

maxi = np.where(np.where([(y2 - np.roll(y2,1) > 0) & (y2 - np.roll(y2,-1) > 0)],y2, 0)> threshold, y2, np.nan)
mini = np.where(np.where([(y2 - np.roll(y2,1) < 0) & (y2 - np.roll(y2,-1) < 0)],y2, 0)<-threshold, y2, np.nan)
'''

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys)

plt.title('Electromyography Data')
plt.xlabel('Data Points (Approximately 860 Reading each Second)' )
plt.ylabel('milliVolts Value Post Gain Adjustment')

'plt(maxi, mini)'


def animate(i, ys):
    
    value = adc.read_adc(3, gain=GAIN)
    
    voltage = (value * scale[GAIN]) / 32767
    milliVolts = voltage * 1000
    
    print("{:.3f} mV" .format(milliVolts))
    time.sleep(0.01)
  
    v=[]
    v = np.loadtxt(EMG_Data2.csv,delimiter=",", dtype=str)
    print("the array is=")
#displaying our result.
    print(v)
    
    peaks = find_peaks(milliVolts, height = 1, threshold = 1, distance = 1)
    height = peaks[1]['peak_heights'] #list of the heights of the peaks
    peak_pos = v[peaks[0]] #list of the peaks positions
    
    ys.append(milliVolts)
    
    ys = ys[-x_len:]

    line.set_ydata(ys)
    
    return line,

ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=1,
    blit=True)
ax.scatter(peak_pos, height, color = 'r', s = 15, marker = 'D', label = 'Maxim')
ax.legend()
ax.grid()
plt.show()





 
