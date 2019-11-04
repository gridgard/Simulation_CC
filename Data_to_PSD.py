import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
import pylab
from scipy import signal as sig
from signal_gen import signal

freq=1000*math.pi*2
fs = 10e3
amp = 1
N = 1e5
noise_power = 0.001*fs /2

t = np.arange(N)/fs

sign = signal(noise_power, freq, amp)

x = sign.real_sig(t)


def PowerSpectrum(d, fs):
    f, Pxx_spec=sig.welch(d, fs)
    return f, Pxx_spec

"""
f, Pxx_spec = PowerSpectrum(x, t)


plt.figure()
plt.xlabel('frequency [Hz]')
plt.ylim([0.5e-3, 1])
plt.semilogy(f, Pxx_spec)
plt.ylabel('Linear spectrum [V^2]')
plt.title('Power spectrum (scipy.signal.welch)')
plt.show()
"""
