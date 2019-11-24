import numpy as np
import pylab
from signal_gen import signal
from scipy import signal as sig
import math
import cmath
import matplotlib.pyplot as plt
import pylab


freq = 400*math.pi*2 #Frequency of sine waves
amp = 1 #Relative amplitude of sine waves
fs = 10e3 # Sample frequency
N = 1000 # Number of samples
noise_power = 0.001 * fs/2 #Amplitude of added noise
t = np.arange(N)/fs #List of the different time intervals for a given N and ts


sign = signal(noise_power, freq, amp) # Initialising the signal from signal_gen, in this case its a sine wave

cc = False 
N0 = 1000 #Number times we take the sum of the dot product of the the fourier transform of one signal on the conjugate of the fourier transform of the other.

i=0 # Counting variable

while (i < N0):
    i+=1
    y_1 = sign.real_sig(t) #Initialise sine wave with noise 1
    y_2 = sign.real_sig(t) #Initialise sine wave with noise 2
    z_1= np.conj(np.fft.fft(y_1)) #Take the complex conjugate of the Fourier transform of signal 1
    z_2 = np.fft.fft(y_1) #Take the fourier transform of 2
    cc_0 = np.multiply(z_1,z_2) #Product of the dot product of the two

    #cc += cc #This should sum the dot products here and give a sum of the cross correlation spectrums.
    if (i==0):
        cc = cc_0
    else:
        cc += cc_0

    

freqs = np.abs(np.fft.fftfreq(t.shape[-1])) # Gives the frequency spectrum of the cross correlation spectrum

maxm = np.max(cc) #Maximum of the cross correlation spectrum


'''
pylab.plot(t,y_1,'r')
pylab.plot(t,y_2,'b')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title("Graph showing sin(x) with noise")
pylab.show()
'''

pylab.plot(fs*freqs,np.log10(cc/N),'r') 
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Log10[Cross Corellation amplitude]')
pylab.title("Cross correlation with {0} summations".format(N0))
pylab.show()



