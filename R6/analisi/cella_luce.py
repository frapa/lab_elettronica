# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt


dati = np.genfromtxt("../dati/luce.csv", delimiter=",", skip_header=1)
I = dati[:,0]
V = dati[:,1]

ids = np.array([v >= 0 for v in V], dtype=np.bool)

Ip = I[ids]
Vp = V[ids]
In = I[np.logical_not(ids)]
Vn = V[np.logical_not(ids)]

matplotlib.rcParams['font.size'] = 15

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7), dpi=65)

# Titolo del grafico
f1.suptitle("Caratteristica di una cella fotovoltaica illuminata",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_axes((0.1, 0.12, 0.3, 0.8))

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=Vn, y=In,
    #yerr=dy, #xerr=,
    fmt='o', c='black', linewidth=3,
    zorder=1)
    
#ax1.set_xlabel(u'Tensione [V]',
#    labelpad=12, fontsize=16)
ax1.set_ylabel(u'Corrente [mA]',
    labelpad=12, fontsize=16)

ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim((-25, 100))
ax1.set_xlim((-55, 0))
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)
#ax1.set_xticklabels((-50, -40, -30, -20, -10, ""))

ax2 = f1.add_axes((0.4, 0.12, 0.57, 0.8))

for label in ax2.get_yaxis().get_majorticklabels():
    label.set_visible(False)

line2 = ax2.errorbar(x=Vp, y=Ip,
    #yerr=dy, #xerr=,
    fmt='o', c='black', linewidth=3,
    zorder=1)
    
ax2.grid(True)
ax2.set_ylim((-25, 100))
ax2.set_xticklabels(("", 0.2, 0.4, 0.4, 0.6, 0.8, 1.0, 1.2))

plt.text(x=0.25, y=-37, s="Tensione [V]")

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.1, right=0.97,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
