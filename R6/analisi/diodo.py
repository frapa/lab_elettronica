# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt


dati = np.genfromtxt("../dati/diodo.csv", delimiter=",", skip_header=2)
I = dati[:,0]
V = dati[:,1]

matplotlib.rcParams['font.size'] = 15

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7), dpi=65)

# Titolo del grafico
f1.suptitle("Caratteristica di un diodo 1N4007",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=V, y=I,
    #yerr=dy, #xerr=,
    fmt='o', c='black', linewidth=3,
    zorder=1)
    
ax1.set_ylabel(u'Tensione [V]',
    labelpad=12, fontsize=16)
ax1.set_xlabel(u'Corrente [mA]',
    labelpad=12, fontsize=16)

ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim((-50, 300))
#ax1.set_xlim((-10, 40))
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)
#ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.12, right=0.97,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show()  
