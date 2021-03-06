# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

from uncertainties import unumpy as unp

import matplotlib
from matplotlib import pyplot as plt

tx = []
ty = []
for i in range(9):
    tx.append(np.genfromtxt("../dati/t{}_1.csv".format(i), delimiter=",", skip_header=2)[:,1])
    ty.append(np.genfromtxt("../dati/t{}_2.csv".format(i), delimiter=",", skip_header=2)[:,1])

x = np.array(tx)
y = np.array(ty)

v5 = []
mxs = []
mys = []
for ax, ay in zip(x, y):
    mx = []
    my = []
    for ex, ey in zip(ax, ay):
        if ex in mx:
            my[mx.index(ex)].append(ey)
        else:
            my.append([ey])
            mx.append(ex)

    mx = np.array(mx)
    my = np.array([np.mean(l) for l in my])
    ind = np.argsort(mx)
    
    mxs.append(mx[ind])
    mys.append(my[ind])

mys = np.array(mys)
mxs = np.array(mxs) - mys


Ib = unp.uarray([1, 2, 3, 4, 5, 6, 7, 8, 9], [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]) * 1e-5
Ic = []
for ibx, iby in zip(mxs, mys):
    for x, y in zip(ibx, iby):
        if 4.95 < x < 5.05:
            Ic.append(y/10)
            break

Ic = unp.uarray(Ic, np.array(Ic) * 0.01)
beta = Ic / Ib
print(beta, np.mean(beta))

matplotlib.rcParams['font.size'] = 15

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 8), dpi=75)

# Titolo del grafico
f1.suptitle("Curve caratteristiche di un transistor",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(111)
# crea plot con le barre d'errore (o anche senza)
#lines = []
#for i in range(9):
#    lines.append(ax1.errorbar(x=x[i], y=y[i]*100.0,
#        fmt='-', c='black', linewidth=3))
lines = []
for i in range(9):
    lines.append(ax1.errorbar(x=mxs[i], y=mys[i]*100.0,
        fmt='-', c='black', linewidth=3))

#lines.append(ax1.errorbar(x=unp.nominal_values(Ib)*1e6, y=unp.nominal_values(beta),
#        fmt='-', c='black', linewidth=3))

ax1.set_xlabel(u'Tensione $V_{ce}$ [V]',
    labelpad=12, fontsize=16)
ax1.set_ylabel(u'Corrente $I_c$ [mA]',
    labelpad=12, fontsize=16)

ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim((0, 47))
ax1.set_xlim((0, 10))
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)
#ax1.set_xticklabels((-50, -40, -30, -20, -10, ""))

ax1.text(8.5, 5.5, u"$I_b$ = 10 μA")
ax1.text(8.8, 10, u"20 μA")
ax1.text(8.5, 15, u"30 μA")
ax1.text(8.2, 20, u"40 μA")
ax1.text(7.8, 25, u"50 μA")
ax1.text(7.5, 30.5, u"60 μA")
ax1.text(7.2, 35.5, u"70 μA")
ax1.text(6.9, 40.5, u"80 μA")
ax1.text(6.6, 45.2, u"90 μA")

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.1, right=0.97,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show()
