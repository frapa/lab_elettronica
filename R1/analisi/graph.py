# -*- encoding: utf-8 -*-

import csv
from math import *

import matplotlib
from matplotlib import pyplot as plt

# tensione monte
vm = ( 
        0.12,
        0.48,
        1.4,
        1.88,
        2.4,
        2.8,
        3.4,
        3.8,
        4.4,
        4.8,
        5.4,
        5.8,
        6.4,
        6.8,
        7.2,
        7.8,
        8.2,
        8.8,
        9.2,
        9.8
)
# corrente monte
im = (
        4.4,
        14,
        17,
        19,
        21,
        23,
        25,
        27,
        29,
        31,
        32,
        34,
        35,
        37,
        39,
        40,
        42,
        43,
        45,
        46,
)
# tensione valle
vv = (
        0.4,
        1,
        1.48,
        2,
        2.6,
        3,
        3.6,
        4,
        4.6,
        5,
        5.6,
        6.2,
        6.6,
        7,
        7.6,
        8,
        8.6,
        9.2,
        9.6
)
# corrente valle
iv = (
        3.9,
        13,
        16,
        18,
        20,
        23,
        25,
        26,
        28,
        29,
        31,
        33,
        35,
        36,
        38,
        39,
        42,
        43,
        44
)

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7))
# Titolo del grafico
f1.suptitle("Corrente in funzione della tensione",
    y=0.96, fontsize=15)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)
# crea plot con le barre d'errore (o anche senza)
dots1 = ax1.errorbar(x=vm, y=im,
    #yerr=dy, #xerr=,
    fmt='o-', c='black')
dots2 = ax1.errorbar(x=vv, y=iv,
    #yerr=dy, #xerr=,
    fmt='o-', c='gray')
#line = ax1.errorbar(x=[-0.8, 0.8], y=[0.05, 0.05],
    #yerr=dy, #xerr=,
#    fmt='-', c='grey')
    
ax1.set_xlabel(u'Tensione [V]',
    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Corrente [mA]',
    labelpad=6, fontsize=14)


ax1.grid(True)
#ax1.set_ylim((0, 1.1))
#ax1.set_xlim((-0.65, 0.65))
# questo produce una legenda
ax1.legend((dots1, dots2), ("Amperometro a monte", "Amperometro a valle"), 'lower right',
    prop={'size': 12})
    
# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.97,
    top=0.88, bottom=0.12, hspace=0, wspace=0.1)

# mostra grafico
plt.show()  

