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

rm = (
     9.8300e+05,
     9.9830e+04,
     9.9370e+03,
     9.9900e+02,
     9.8880e+01,
     9.9700e+00,
     1.0400e+00,
)

rv = (
      9.8300e+05,
      9.9830e+04,
      9.9370e+03,
      9.9900e+02,
      9.8880e+01,
      9.9700e+00,
      1.0400e+00,
)


acm = (
   5.0000e+05,
   8.9286e+04,
   1.0000e+04,
   9.8824e+02,
   9.8824e+01,
   1.0333e+01,
   9.5238e-01,
)

dacm = (
    8.0778e+03,
    1.3837e+03,
    1.6348e+02,
    1.8122e+01,
    1.8122e+00,
    2.6683e-01,
    5.6540e-02,
)

m = (
   1.0000e+06,
   9.8039e+04,
   1.0101e+04,
   1.0133e+03,
   9.9068e+01,
   1.0336e+01,
   9.5240e-01,
)

dm = (
   3.2311e+04,
   1.6683e+03,
   1.6680e+02,
   1.9052e+01,
   1.8212e+00,
   2.6696e-01,
   5.6543e-02,
)

acv = (
   1.0000e+06,
   1.0000e+05,
   1.0000e+04,
   1.0588e+03,
   1.0588e+02,
   1.1667e+01,
   2.3529e+00,
)

dacv = (
    2.0435e+04,
    1.6348e+03,
    1.6348e+02,
    1.9240e+01,
    1.9240e+00,
    2.9700e-01,
    7.8842e-02,
)

v = (
   9.9800e+05,
   9.9411e+04,
   9.9365e+03,
   9.9534e+02,
   9.9487e+01,
   5.2718e+00,
   1.7130e+00,
)

dv = (
   2.0435e+04,
   1.6348e+03,
   1.6348e+02,
   1.9240e+01,
   1.9240e+00,
   2.9700e-01,
   7.8842e-02,
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

##########################################################################à
# Creo un grafico la dimensione è in pollici
f2 = plt.figure(figsize=(10, 7))
# Titolo del grafico
f2.suptitle('Resistenza "vera" e misurata',
    y=0.96, fontsize=15)

# GRAFICO 1
ax2 = f2.add_subplot(1, 1, 1)
ax2.set_yscale('log')
ax2.set_xscale('log')
# crea plot con le barre d'errore (o anche senza)
dots_m = ax2.errorbar(x=rm, y=m,
    yerr=dm, #xerr=,
    fmt='o-', color="#000000")
dots_acm = ax2.errorbar(x=acm, y=m,
    yerr=dacm, #xerr=,
    fmt='o--', color="#000000")

dots_v = ax2.errorbar(x=rv, y=v,
    yerr=dv, #xerr=,
    fmt='o-', color="#777777")
dots_acv = ax2.errorbar(x=acv, y=v,
    yerr=dacv, #xerr=,
    fmt='o:', color="#000000")
    
ax2.set_xlabel(u'Resistenza "vera" [Ω]',
    labelpad=12, fontsize=14)
ax2.set_ylabel(u'Resistenza misurata [Ω]',
    labelpad=6, fontsize=14)


ax2.grid(True)
ax2.set_ylim((0.5, 2e6))
ax2.set_xlim((0.5, 2e6))
# questo produce una legenda
ax2.legend((dots_m, dots_acm, dots_v, dots_acv), 
    ("Amperometro a monte", "Senza correzione - monte", "Amperometro a valle", "Senza correzione - valle"),
    'lower right', prop={'size': 15})
    
# questo imposta i bordi del grafico
f2.subplots_adjust(left=0.1, right=0.97,
    top=0.88, bottom=0.12, hspace=0, wspace=0.1)


# mostra grafico
plt.show()  

