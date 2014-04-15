# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt


dati = np.genfromtxt("../dati/buio.csv", delimiter=",", skip_header=2)
I = dati[:,0]
V = dati[:,1]

ids = np.array([v > 0 for v in V])

Ip = I[ids]
Vp = V[ids]
In = I[np.logical_not(ids)]
Vn = V[np.logical_not(ids)]

matplotlib.rcParams['font.size'] = 15

### CELLA-BUIO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7), dpi=65)

# Titolo del grafico
f1.suptitle("Caratteristica I-V di una cella fotovoltaica al buio",
    y=0.97, fontsize=17)

# GRAFICO 1 ##########
ax1 = f1.add_axes((0.1, 0.12, 0.3, 0.8))

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=Vn, y=In,
    #yerr=dy, #xerr=,
    fmt='o', c='black', linewidth=3,
    zorder=1)

ax1.set_ylabel(u'Intensità [mA]',
    labelpad=12, fontsize=16)
#ax1.set_xlabel(u'Tensione [V]',
#    labelpad=12, fontsize=16)

ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim((-10, 100))
ax1.set_xlim((-55, 0))
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)
#ax1.set_xticklabels(("", -50, -40, -30, -20, -10))

# GRAFICO 2 ##########
ax2 = f1.add_axes((0.4, 0.12, 0.57, 0.8))

# crea plot con le barre d'errore (o anche senza)
line = ax2.errorbar(x=Vp, y=Ip,
    #yerr=dy, #xerr=,
    fmt='o', c='black', linewidth=3,
    zorder=1)

#ax2.set_ylabel(u'Intensità [mA]',
#    labelpad=12, fontsize=16)
#ax2.set_xlabel(u'Tensione [V]',
#    labelpad=12, fontsize=16)

ax2.grid(True)
#ax1.set_xscale('log')
ax2.set_ylim((-10, 100))
ax2.set_xlim((0, 7.5))
#ax2.set_xlim((-60, 0))
for label in ax2.get_yaxis().get_majorticklabels():
   label.set_visible(False)
#ax2.set_xticklabels(("", 0.2, 0.4, 0.6, 0.8, 1.0, 1.2))

# questo produce una legenda
#ax1.legend((line, line_corr),
 #   ("Tensione ai capi dell'interruttore", "Tensione in ingresso"), 'upper left',
 #   prop={'size': 13})


# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.12, right=0.97,
    top=0.92, bottom=0.10, hspace=0.08, wspace=0)
    
### Aggiungere testo a caso XD
plt.text(x=0.25, y=-20, s='Tensione [V]' )

# mostra grafico
plt.show()  
