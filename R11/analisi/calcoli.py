#! -*- encoding: utf-8 -*-

from math import *
import numpy as np

from uncertainties import ufloat, unumpy

from matplotlib import pyplot as plt

def g_1000hz():
    g_1000hz = np.genfromtxt("../dati/g_1000hz.csv", skip_header=1, delimiter=",")
    vin = unumpy.uarray(g_1000hz[:,0] * 0.001, g_1000hz[:,1] * 0.001)
    vout = unumpy.uarray(g_1000hz[:,2], g_1000hz[:,3])

    Gs = vout / vin
    G = sum(Gs) / float(len(Gs))

    print Gs, "\n", G, 

def g_515mv():
    g_515mv = np.genfromtxt("../dati/g_515mv.csv", skip_header=1, delimiter=",")
    freq = unumpy.uarray(g_515mv[:,0], 0.01 * g_515mv[:,0]) * 1000
    vout = unumpy.uarray(g_515mv[:,1], g_515mv[:,2])
    fase = unumpy.uarray(g_515mv[:,3], g_515mv[:,4])

    vin = ufloat(0.515, 0.005)

    Gs = vout / vin
    
    print Gs

    f = plt.figure(figsize=(8, 8))
    f.suptitle("Amplificatore invertente", fontsize=15, y=0.98)
    
    ax = f.add_subplot(211)

    ax.errorbar(x=unumpy.nominal_values(freq),
        y=unumpy.nominal_values(Gs),
        c='black', fmt='o-')

    ax.set_xlabel('Frequenza', fontsize=14)
    ax.set_ylabel('Guadagno G', fontsize=14)

    ax.set_xscale('log')
    ax.set_yticklabels(('', 2, 3, 4, 5, 6, 7, 8, 9, 10))
    ax.set_xticklabels(('', '100 hz', u"1 kHz", u"10 kHz", u"100 kHz", u"1 MHz"))
    ax.grid(True)
    
    ax2 = f.add_subplot(212)

    ax2.errorbar(x=unumpy.nominal_values(freq),
        y=unumpy.nominal_values(fase),
        c='black', fmt='o-')

    ax2.set_ylabel('Sfasamento [Gradi]', fontsize=14)

    ax2.set_xscale('log')
    ax2.set_xticklabels(('', '', u"1 kHz", u"10 kHz", u"100 kHz", u"1 MHz"))
    ax2.grid(True)

    ax3 = ax2.twiny()
    ax3.set_xticks((0, 0.25, 0.5, 0.75, 1))
    ax3.set_xticklabels(('', "1 kHz", u"10 kHz", u"100 kHz", u"1 MHz"))

    f.subplots_adjust(top=0.93, hspace=0.25, bottom=0.07, right=0.95)

    plt.savefig("../latex/amp_inv.pdf")

    plt.show()

g_1000hz()
g_515mv()
