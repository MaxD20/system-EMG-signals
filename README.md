system-EMG-signals

The acquisition system for electromyographic signals consists in a Python algorithm that read the muscle contraction input from the user through gelled electrodes and display in real time the amplified muscle contraction through Grove EMG detector sensor. 

In addition, the system stands out for some main reasons: the usage of hand gestures that can be further processed for a prosthetic limb or rehabilitation exercises for wrist stain, the detection of zygomaticus muscle’s signal that can be plotted in order to differentiate a relieved person from a stressed pacient and the eye blink electromyography which can be very useful among persons that suffers from face paralysis and are trying to communicate with the relatives by eyes movement, as so common phrase “blink once for yes, blink twice for no”. 

Nevertheless, the acquisition system also has a part of peek detection algorithm whose purpose is to highlight signal’s spikes with greater amplitude from regular ones and from noise.

<img src="https://github.com/user-attachments/assets/ad457247-c338-4ce5-a8e3-7d0388a98ede" width="400" height="300">

EMG of Open Hand<br>
<img src="https://github.com/user-attachments/assets/8f7260e0-1990-4aab-ac0f-043a5f94e508" width="400" height="100" alt = "EMG of Open Hand" title = "EMG of Open Hand">
</br>
EMG of Closed Hand<br>
<img src="https://github.com/user-attachments/assets/b3dfe7b2-7da2-48ef-8727-7c1fcf5f5458" width="400" height="50%"><br>
EMG of Bicep</br>

The peak detection method is aiming to mark a red dot on the amplitude of electromyographic signal. For this procedure I used the scipy.signal.find_peaks, a function that take one dimension array and find the maximum by comparing the neighbour values. In the down below figure is observed four consequently contractions of the right-arm bicep, performed from 0 to 6000 milliseconds. The first contraction is noisier due to the friction of the gel electrodes with the surface and the air.<br>
<img src="https://github.com/user-attachments/assets/bf92f8ce-0b7c-4f15-b8a8-c555c6744998" width="400" height="10%"></br>
Peaks from bicep electromyography

<img src="https://github.com/user-attachments/assets/824b5148-2c5a-4ddb-b879-1059b4efcbb4" width="30%" height="30%"><br>
EMG Hand Gestures
