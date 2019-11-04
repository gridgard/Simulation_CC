import math
import cmath
import matplotlib.pyplot as plt
import numpy as np
import pylab
from random import uniform

class signal(object):
    def __init__(self, noisev, w0,a):
        self.noiseV = noisev
        self.w0 = w0
        self.a=a

    def sig(self, t):
        self.value = self.a*math.sin(self.w0*t)

    def noise_sig(self):
        delta = self.noiseV 
        self.value += uniform(-delta, delta)
        return self.value

    def real_sig(self, ts):
        result = []
        for t in ts:
            self.sig(t)
            result.append(self.noise_sig())
        return np.array(result)
