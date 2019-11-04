import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
import pylab
from signal_gen import signal
from scipy import signal as sig


def PowerSpectrum(d, fs):
    f, Pxx_spec=sig.welch(d, fs)
    return f, Pxx_spec

freq=1000*math.pi*2
fs = 10e3 
amp = 1
N = 1e5
noise_power = 0.001*fs /2

t = np.arange(N)/fs

sign = signal(noise_power, freq, amp)

y= sign.real_sig(t)



f, Pxx = PowerSpectrum(y,fs)

pylab.plot(t,y,'-')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title("Graph showing sin(x) with noise")
pylab.show()

plt.figure()
plt.xlabel('frequency [Hz]')
#plt.ylim([0.5e-3, 1])
plt.semilogy(f, Pxx)
plt.ylabel('Linear spectrum [V^2]')
plt.title('Power spectrum (scipy.signal.welch)')
plt.show()
