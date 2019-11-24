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
fs = 1e5 # Sample frequency
N = 10000 # Number of samples
noise_power = 0.5 #Amplitude of added noise
t = np.arange(N)/fs #List of the different time intervals for a given N and ts
NSum = 100 #Number of repeated summations
P = False 
cc = False 
N0 = np.arange(NSum) #Number times we take the sum of the dot product of the the fourier transform of one signal on the conjugate of the fourier transform of the other.
i=0 # Counting variable
for i in range(0,NSum) :
    sign = signal(noise_power, freq, amp) # Initialising the signal from signal_gen, in this case its a sine wave
    y_1 = sign.real_sig(t) #Initialise sine wave with noise 1
    z_1= np.conj(np.fft.fft(np.multiply(np.hanning(N),y_1),norm = None)/N) #Take the complex conjugate of the Fourier transform of signal 1
    z_2 = np.fft.fft(np.multiply(np.hanning(N),y_1), norm = None)/N #Take the fourier transform of 2
    cc_0 = np.multiply(z_1,z_2) #Product of the dot product of the two

    f, Pxx = sig.welch(y_1, fs = fs, nperseg = N, scaling = 'density')
    
    if (i==0):
        cc = cc_0
        P = Pxx
    else:
        cc += cc_0 #cc += cc_0 #This should sum the dot products here and give a sum of the cross correlation spectrums.
        P += Pxx
freqs = np.fft.rfftfreq(t.shape[-1]) # Gives the frequency spectrum of the cross correlation spectrum
P = np.sqrt(P/float(NSum))
cc = 2*np.sqrt(2*np.sqrt(np.multiply(cc,np.conj(cc))/float(NSum**2))/(fs*1.5/N))
pylab.loglog(fs*freqs,cc[0:int((N/2)+1)],'r', label = 'FFT')
pylab.loglog(f,P,'b', label='Welch')
pylab.legend()
pylab.xlabel('Frequency [Hz]')
pylab.ylabel('Cross Corellation amplitude')
pylab.title("Cross correlation with {0} summations".format(NSum))
pylab.show()






