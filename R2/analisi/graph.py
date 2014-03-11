# -*- encoding: utf-8 -*-

import csv
from math import *

import matplotlib
from matplotlib import pyplot as plt

import numpy as np

data = np.genfromtxt("../dati/rabdon.csv", delimiter=',', skip_header=1)
t = data[:,0]
q = data[:,1]
v = data[:,2]

data2 = np.genfromtxt("../dati/uk.csv", delimiter=',', skip_header=1)
t2 = data2[:,0]
q2 = data2[:,1]
v2 = data2[:,2]

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7))
# Titolo del grafico
f1.suptitle("Corrente in funzione della tensione",
    y=0.96, fontsize=15)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)
# crea plot con le barre d'errore (o anche senza)
dots1 = ax1.errorbar(x=t, y=v,
    #yerr=dy, #xerr=,
    fmt='-', c='black')
line = ax1.errorbar(x=t, y=q,
    #yerr=dy, #xerr=,
    fmt='--', c='black')
    
ax1.set_xlabel(u'Tempo [ms]',
    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Tensione [V]',
    labelpad=6, fontsize=14)


ax1.grid(True)
ax1.set_ylim((-0.05, 1.05))
ax1.set_xlim((-0.004, 0.01))
ax1.set_xticklabels((-4, -2, 0, 2, 4, 6, 8, 10))
# questo produce una legenda
ax1.legend((dots1, line), ("Tensione ai capi", "Tensione fornita"), 'lower right',
    prop={'size': 12})

ax1.plot([2.08e-3, 2.08e-3], [-0.5, 0.632], linestyle="-.", color="black")
    

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.08, right=0.96,
    top=0.88, bottom=0.12, hspace=0, wspace=0.15)

# mostra grafico
plt.show()  

