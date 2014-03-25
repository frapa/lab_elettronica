# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

arg = np.vectorize(cmath.phase)

############## PASSA-BASSO ################################
dati = np.genfromtxt("../dati/filtro.csv", skip_header=1, delimiter=",")
freq = dati[:,0]
vin = 5000
vout = dati[:,1]
ph = -dati[:,2]

dB = 20 * np.log10(vout / vin)

R = 1000
C1 = 102.9e-9
C3 = 100.9e-9

f = np.logspace(1, 6, num=500)
w = 2 * pi * f

Zd = 2*R
Zs = R - 1j / (w * C1) + (1/R + 1j*w*C3)**-1

Id = vin / Zd
Is = vin / Zs

V2 = vin - R*Id
V1 = vin - (R - 1j / (w * C1)) * Is

dV = V1 - V2
tV = np.abs(dV)
tph = arg(V1) * 180 / pi
aph = arg(V2 - V1) * 180 / pi

tdB = 20 * np.log10(tV/vin)

print(w[150])
t = np.linspace(0, 0.01, num=100)
ff = plt.figure(figsize=(9.5, 10), dpi=65)
# GRAFICO 1
ax = ff.add_subplot(1, 1, 1)
print(abs(V1[150]), V2)
ax.errorbar(x=t, y=(V1[150]*np.exp(1j*w[150]*t)).real)
ax.errorbar(x=t, y=(V2*np.exp(1j*w[150]*t)).real)
ax.grid(True)

A = (w * R * C1)**2
rV = np.sqrt(A**4 + 6*A**3 - 5*A**2 + 6*A + 1) / (2*A**2 + 14*A + 2)
adB = 20 * np.log10(rV)

############### GRAFICO ###################################
matplotlib.rcParams['font.size'] = 15

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(9.5, 10), dpi=65)

# Titolo del grafico
f1.suptitle("Filtro notch con ponte di Wien",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=f, y=tdB,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3)

line = ax1.errorbar(x=f, y=adB,
    #yerr=dy, #xerr=,
    fmt='-', c='blue', linewidth=3)

dots1 = ax1.errorbar(x=freq, y=dB,
    #yerr=db_dB, #xerr=,
    fmt='o', c="white", linewidth=2,
    markersize=7, markeredgewidth=1)
    
ax1.set_ylabel(u'Attenuazione [dB]',
    labelpad=12, fontsize=16)


ax1.grid(True)
ax1.set_xscale('log')
ax1.set_ylim((-17, -5))
ax1.set_xlim((40, 1.2e5))
for label in ax1.get_xaxis().get_majorticklabels():
  label.set_visible(False)
#ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))

# GRAFICO 2
ax2 = f1.add_subplot(2, 1, 2)

# crea plot con le barre d'errore (o anche senza)
line2 = ax2.errorbar(x=f, y=tph,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3)

line21 = ax21.errorbar(x=f, y=aph,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3)

dots2 = ax2.errorbar(x=freq, y=ph,
    #yerr=dy, #xerr=,
    fmt='o', c='white', linewidth=2,
    markersize=7, markeredgewidth=1)
    
ax2.set_xlabel(u'Frequenza [Hz]',
    labelpad=12, fontsize=16)
ax2.set_ylabel(u'Sfasamento [gradi]',
    labelpad=12, fontsize=16)


ax2.grid(True)
ax2.set_xscale('log')
ax2.set_ylim((-95, 95))
ax2.set_xlim((40, 1.2e5))
ax2.set_yticks((-90, -67.5, -45, -22.5, 0, 22.5, 45, 67.5, 90))

# questo produce una legenda
#ax2.legend((dots1, line, line_corr), ("Punti sperimentali", "Previsione teorica", "Correzione"), 'upper right',
#    prop={'size': 15})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.12, right=0.97,
    top=0.92, bottom=0.09, hspace=0.08, wspace=0)

# mostra grafico
plt.show()  
