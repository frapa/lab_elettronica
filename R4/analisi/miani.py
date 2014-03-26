# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

#### incertezze sule resistenze all'5% #####

R1 = 1926
dR1 = 1
R2 = 2000
dR2 = 100 
R3 = 1000
dR3 = 50
R4 = 1000
dR4 = 50
C4 = 102.9e-9
dC4 = 0.1e-9

f = 9100
df = f * 0.01

w = 2 * pi * f
dw = sqrt( (df)**2 * (2 * pi) )

vin = 5

ZC4 = 1j / (w * C4)

Zd = R2 + R4 + ZC4
Id = vin / Zd

C3 = (R2/R1 - R4/R3) * C4
dC3 = sqrt(
                ( (dR1)*((R2*C4)/(R1**2)) )**2 +
                ( (dR2)*(C4/R1) )**2 +
                ( (dR3)*((R4*C4)/(R3**2)) )**2 +
                ( (dR4)*(C4/R3) )**2 +
                ( (dC4)*(R2/R1 - R4/R3))**2
          )
          
print(( (dR1)*((R2*C4)/(R1**2)) )**2)
print(( (dR2)*(C4/R1) )**2)
print(( (dR3)*((R4*C4)/(R3**2)) )**2)
print(( (dR4)*(C4/R3) )**2)
print(( (dC4)*(R2/R1 - R4/R3))**2)

print()
### Questi valori rompono le palle!!! ###
print( ((dR2)**2)*((C4/R1)**2) )

print()

C3_1 = 1/(w**2)*1/(R3*R4*C4)
dC3_1 = sqrt( 
                ( (dw)*(2/(R3*R4*C4*(w)**3)) )**2 +
                ( (dR3)*(1/(R4*C4)*1/(w*R3)**2) )**2 +
                ( (dR4)*(1/(R3*C4)*1/(w*R4)**2) )**2 +
                ( (dC4)*(1/(R3*R4)*1/(w*C4)**2) )**2
            )
            
print(( (dw)*(2/(R3*R4*C4*(w)**3)) )**2)
print(( (dR3)*(1/(R4*C4)*1/(w*R3)**2) )**2)
print(( (dR4)*(1/(R3*C4)*1/(w*R4)**2) )**2)
print(( (dC4)*(1/(R3*R4)*1/(w*C4)**2) )**2)

print()

print(C3)
print(dC3)
print()
print(C3_1)
print(dC3_1)
