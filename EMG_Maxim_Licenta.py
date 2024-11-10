import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
y_range = [0, 2250]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = list(range(0, x_len))
ys = [0] * x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys)

plt.title('Electromyography Data')
plt.xlabel('Data Points (Approximately 128 Reading each Second)' )
plt.ylabel('milliVolts Value Post Gain Adjustment')


def animate(i, ys):
    
    value = adc.read_adc(3, gain=GAIN)
    
    voltage = (value * scale[GAIN]) / 32767
    milliVolts = voltage * 1000
    
    print("{:.3f} mV" .format(milliVolts))
   
#while True:
    if milliVolts < 1470:
        GPIO.output(9, GPIO.LOW) 
        GPIO.output(25, GPIO.LOW) 
        GPIO.output(10, GPIO.LOW)
        GPIO.output(21, GPIO.LOW) 
        GPIO.output(24, GPIO.LOW) 
        GPIO.output(23, GPIO.LOW) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)  
        
    
    elif milliVolts > 1470 and milliVolts < 1500:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.LOW) 
        GPIO.output(10, GPIO.LOW)
        GPIO.output(21, GPIO.LOW) 
        GPIO.output(24, GPIO.LOW) 
        GPIO.output(23, GPIO.LOW) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
        
        
    elif milliVolts > 1500 and milliVolts < 1550:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.LOW)
        GPIO.output(21, GPIO.LOW) 
        GPIO.output(24, GPIO.LOW) 
        GPIO.output(23, GPIO.LOW) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
        
    
    elif milliVolts > 1550 and milliVolts < 1570:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW) 
        GPIO.output(24, GPIO.LOW) 
        GPIO.output(23, GPIO.LOW) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
        
        
    elif milliVolts > 1570 and milliVolts < 1600:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.LOW) 
        GPIO.output(23, GPIO.LOW) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
       
        
    elif milliVolts > 1600 and milliVolts < 1630:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.HIGH) 
        GPIO.output(23, GPIO.LOW) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
    
        
    elif milliVolts > 1630 and milliVolts < 1660:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.HIGH) 
        GPIO.output(23, GPIO.HIGH) 
        GPIO.output(22, GPIO.LOW) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
      
    
    elif milliVolts > 1660 and milliVolts < 1690:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.HIGH) 
        GPIO.output(23, GPIO.HIGH) 
        GPIO.output(22, GPIO.HIGH) 
        GPIO.output(27, GPIO.LOW) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
       
        
    elif milliVolts > 1690 and milliVolts < 1700:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.HIGH) 
        GPIO.output(23, GPIO.HIGH) 
        GPIO.output(22, GPIO.HIGH) 
        GPIO.output(27, GPIO.HIGH) 
        GPIO.output(18, GPIO.LOW) 
        GPIO.output(17, GPIO.LOW)
      
         
    elif milliVolts > 1700 and milliVolts < 1730:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.HIGH) 
        GPIO.output(23, GPIO.HIGH) 
        GPIO.output(22, GPIO.HIGH) 
        GPIO.output(27, GPIO.HIGH) 
        GPIO.output(18, GPIO.HIGH) 
        GPIO.output(17, GPIO.LOW)
       
         
    elif milliVolts > 1730 and milliVolts < 1750:
        GPIO.output(9, GPIO.HIGH) 
        GPIO.output(25, GPIO.HIGH) 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH) 
        GPIO.output(24, GPIO.HIGH) 
        GPIO.output(23, GPIO.HIGH) 
        GPIO.output(22, GPIO.HIGH) 
        GPIO.output(27, GPIO.HIGH) 
        GPIO.output(18, GPIO.HIGH) 
        GPIO.output(17, GPIO.HIGH)
       
    
    ys.append(milliVolts)
    
    ys = ys[-x_len:]
    
    line.set_ydata(ys)
    
    
    return line,
    
    GPIO.cleanup()
    sys.exit()

ani = animation.FuncAnimation(fig,
    animate,
    fargs=(ys,),
    interval=1,
    blit=True)
ax.grid()
plt.show()





 