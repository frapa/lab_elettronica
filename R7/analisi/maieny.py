# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

### resistenza dinamica ###

k = (70.3743956043956) * 0.001
dk = (0.52590865925967) * 0.001
Rd = 1/k
dRd = ( ((dk)**2)*(1/(k)**2)**2 )**(1/2)

print(Rd)
print(dRd)
print()

### rapporto di stabilizzazione ###

R = 1000
dR = 50 ## errore su R del 5%

c_teo = (Rd)/(R+Rd)
dc_teo = ( (((1/(R+Rd))+((Rd)/(R+Rd)**2))**2)*(dRd)**2 + ((Rd/(R+Rd)**2)**2)*(dR)**2 )**(1/2)

print(c_teo)
print(dc_teo)
print()
