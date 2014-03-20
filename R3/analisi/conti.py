# -*- encoding: utf-8 -*-

from math import *
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

############## PASSA-BASSO ################################
basso = np.genfromtxt("../dati/passa_basso.csv", skip_header=1, delimiter=",")
b_vin = basso[:,0]
b_vout = basso[:,1]
b_ph = basso[:,2]
b_freq = basso[:,3]

b_dB = 20 * np.log10(b_vout / b_vin)

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(8, 9))
# Titolo del grafico
f1.suptitle("Corrente in funzione della tensione",
    y=0.96, fontsize=15)

# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)
# crea plot con le barre d'errore (o anche senza)
dots1 = ax1.errorbar(x=b_freq, y=b_dB,
    #yerr=dy, #xerr=,
    fmt='o-', c='gray', linewidth=2)
#line = ax1.errorbar(x=t, y=q,
    #yerr=dy, #xerr=,
#    fmt='--', c='black')
    
#ax1.set_xlabel(u'Frequenza [Hz]',
#    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Attenuazione [dB]',
    labelpad=6, fontsize=14)


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

ax1.plot((796, 795), (-30, 2), color="black")

# GRAFICO 2
ax2 = f1.add_subplot(2, 1, 2)
# crea plot con le barre d'errore (o anche senza)
dots2 = ax2.errorbar(x=b_freq, y=b_ph,
    #yerr=dy, #xerr=,
    fmt='o-', c='gray', linewidth=2)
#line = ax1.errorbar(x=t, y=q,
    #yerr=dy, #xerr=,
#    fmt='--', c='black')
    
ax2.set_xlabel(u'Frequenza [Hz]',
    labelpad=12, fontsize=14)
ax2.set_ylabel(u'Sfasamento [gradi]',
    labelpad=6, fontsize=14)


ax2.grid(True)
ax2.set_xscale('log')
ax2.set_ylim((0, 90))
ax2.set_xlim((40, 30000))
#ax1.set_xticklabels((-4, -2, 0, 2, 4, 6, 8, 10))
# questo produce una legenda
#ax1.legend((dots1, line), ("Tensione ai capi", "Tensione fornita"), 'lower right',
#    prop={'size': 12})

ax2.plot((796, 795), (0, 90), color="black")

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.1, right=0.96,
    top=0.91, bottom=0.09, hspace=0.05, wspace=0)

# mostra grafico
plt.show()  
