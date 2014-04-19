# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np
from numpy import *

import matplotlib
from matplotlib import pyplot as plt

#Capacità	500 nF	1 uF	2 uF	5 uF	3 uF
#Ampiezza picco-picco	6.8 V	4.8 V	3.2 V	1.6 V	2.4 V
#Freq (Hz)	100 Hz	100 Hz	100 Hz	100 Hz	100 Hz
#Media	6.898 V	7.73 V	8.47 V	9.07 V	8.78 V

Vr = array([6.8, 4.8, 3.2, 2.4, 1.6])
Vm = array([6.898, 7.73, 8.47, 8.78, 9.07])
dVr = array([0.1, 0.1, 0.1, 0.1, 0.1])
dVm = array([0.001, 0.01, 0.01, 0.01, 0.01])

r = Vr/Vm
dr = ( (((1/Vm)*(dVr))**2 + (((Vr)/((Vm)**2))*(dVm))**2)**(1/2) )

print(r)
print()
print(dr)
