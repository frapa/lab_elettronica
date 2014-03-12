# -*- encoding: utf-8 -*-

from math import *
import numpy as np

R = np.array((19943, 997, 499550))
dR = np.array((19943, 997, 499550)) * 0.05
C = np.array((99.3e-9, 990e-9, 5e-9))
dC = np.array((99.3e-9, 990e-9, 5e-9)) * 0.05

T = R * C
dT = np.sqrt((dR * C)**2 + (R * dC)**2)
print(T, dT)

C_inc = 3.04e-3 / 3e3
print(C_inc)
