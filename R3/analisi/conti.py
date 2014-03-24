# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

############## PASSA-BASSO ################################
basso = np.genfromtxt("../dati/passa_basso.csv", skip_header=1, delimiter=",")
b_vin = basso[:,0]
b_vout = basso[:,1]
b_ph = -basso[:,2]
b_freq = basso[:,3]

R = 1000
dR = 10
C = 200e-9
dC = C * 0.01
taglio = 1/(2*pi*R*C)
dtaglio = sqrt((1/(2*pi)*(R*C)**-2)**2 * (C**2*dR**2 + R**2*dC**2)) 
print(taglio, "±", dtaglio)

b_dB = 20 * np.log10(b_vout / b_vin)

f = np.logspace(1, 5, num=500)
w = 2*pi*f
I = 1 / (R - 1j/(w*C))
V = 1 - R*I
out = abs(V)
phase = np.vectorize(cmath.phase)
ph = phase(V) * 180 / pi
t_dB = 20 * np.log10(out)

matplotlib.rcParams['font.size'] = 15
### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(9.5, 10), dpi=65)
# Titolo del grafico
f1.suptitle("Filtro passa-basso",
    y=0.96, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)

ax1.plot((796, 796), (-30, 2), color="black", linewidth=2)

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=f, y=t_dB,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3)
dots1 = ax1.errorbar(x=b_freq, y=b_dB,
    #yerr=dy, #xerr=,
    fmt='o', c="white", linewidth=2,
    markersize=7, markeredgewidth=1)
    
#ax1.set_xlabel(u'Frequenza [Hz]',
#    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Attenuazione [dB]',
    labelpad=10, fontsize=16)


ax1.grid(True)
ax1.set_xscale('log')
ax1.set_ylim((-30, 2))
ax1.set_xlim((40, 30000))
for label in ax1.get_xaxis().get_majorticklabels():
  label.set_visible(False)
ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))
# questo produce una legenda
#ax1.legend((dots1, line), ("Tensione ai capi", "Tensione fornita"), 'lower right',
#    prop={'size': 12})


# GRAFICO 2
ax2 = f1.add_subplot(2, 1, 2)

ax2.plot((796, 796), (-90, 0), color="black", linewidth=2)

# crea plot con le barre d'errore (o anche senza)
line2 = ax2.errorbar(x=f, y=ph,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3)
dots2 = ax2.errorbar(x=b_freq, y=b_ph,
    #yerr=dy, #xerr=,
    fmt='o', c="white", linewidth=2,
    markersize=7, markeredgewidth=1)
    
ax2.set_xlabel(u'Frequenza [Hz]',
    labelpad=12, fontsize=16)
ax2.set_ylabel(u'Sfasamento [gradi]',
    labelpad=10, fontsize=16)


ax2.grid(True)
ax2.set_xscale('log')
ax2.set_ylim((-90, 0))
ax2.set_xlim((40, 30000))
#ax1.set_xticklabels((-4, -2, 0, 2, 4, 6, 8, 10))
# questo produce una legenda
ax2.legend((dots1, line,), ("Punti sperimentali", "Previsione teorica"), 'upper right',
    prop={'size': 15})
    
ax2.text(740, 2, "ν₀ = 800 ± 10")

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.12, right=0.97,
    top=0.92, bottom=0.09, hspace=0.08, wspace=0)

# mostra grafico
plt.show()  
