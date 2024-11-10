import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 1
scale = {2/3: 6.144,
         1 : 4.096,
         2 : 2.048,
         4 : 1.024,
         8 : 0.512,
         16 : 0.256}

start = 0

numSamples = 500

f = open('EMG_Data2.csv', 'w')

t0 = time.time()

for sampleIndex in range(numSamples):
    value = adc.read_adc(3, gain=GAIN)
    voltage = value * scale[GAIN] / 32767
    milliVolts = voltage * 1000
    print ("{: .0f} ".format(milliVolts))
    
    f.write(("{: .0f} ".format(milliVolts))+'\n')
    
t1=time.time()
total=t1-t0

print('This is the time in seconds it took to complete data collection '+ str(total))

#This is to finalise the text file manipulations. Once below happens nothing will alter the text file.
f.close()
        
