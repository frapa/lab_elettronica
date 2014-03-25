# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

R2 = 2000
R4 = 1000
C4 = 102.9e-9
R1 = 1926
R3 = 1000
dR = 50

f = 9100
w = 2 * pi * f
vin = 5

ZC4 = 1j / (w * C4)

Zd = R2 + R4 + ZC4
Id = vin / Zd

C3 = (R2/R1 - R4/R3) * C4
dC3 = 
print(C3)
