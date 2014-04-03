# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt


ms = (
    6.6, 21, 5.8, 9, 5, 16.2, 17, 20.8, 12, 4.6, 5.4, 9.8,
    16, 9.6, 4.8, 9, 8.2, 8.8, 8.4, 9.2
)

print(np.mean(ms), np.std(ms))

dati = np.genfromtxt("../dati/n1.csv", delimiter=",", skip_header=2)
t = dati[:,0] * 1000
v1 = dati[:,1] / 2
v2 = dati[:,2] / 2


matplotlib.rcParams['font.size'] = 15

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7), dpi=65)

# Titolo del grafico
f1.suptitle("Tempo di reazione di un interruttore differenziale",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=t, y=v1,
    #yerr=dy, #xerr=,
    fmt='-', c='red', linewidth=3,
    zorder=1)

line_corr = ax1.errorbar(x=t, y=v2,
    #yerr=dy, #xerr=,
    fmt='-', c='black', linewidth=2,
    zorder=1)
    
ax1.set_ylabel(u'Tensione [V]',
    labelpad=12, fontsize=16)
ax1.set_xlabel(u'Tempo [ms]',
    labelpad=12, fontsize=16)

ax1.grid(True)
#ax1.set_xscale('log')
#ax1.set_ylim((-17, -5))
ax1.set_xlim((-10, 40))
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)
#ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))

# questo produce una legenda
ax1.legend((line, line_corr),
    ("Tensione ai capi dell'interruttore", "Tensione in ingresso"), 'upper left',
    prop={'size': 13})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.12, right=0.97,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show()  
