# -*- encoding: utf-8 -*-

from math import *
import cmath
import numpy as np

import matplotlib
from matplotlib import pyplot as plt

arg = np.vectorize(cmath.phase)

############## PASSA-BASSO ################################
dati = np.genfromtxt("../dati/filtro.csv", skip_header=1, delimiter=",")
freq = dati[:,0]
dfreq = freq * 0.01
vin = 2.500
dvin = vin * 0.01
vout = dati[:,1] * 0.0005
dvout = vout * 0.01
ph = -dati[:,2] / 180 * pi
dph = ph * 0.01

dB = 20 * np.log10(vout / vin)
ddB = 20 * np.sqrt((dvout/vout)**2 + (dvin/vin)**2)

########## CORREZIONE DEI DATI SPERIMENTALI ##########################
R = 1000
dR = R * 0.05
C1 = 102.9e-9
dC1 = 0.1e-9
C3 = 100.9e-9
dC3 =0.1e-9

w_exp = 2 * pi * freq
dw_exp = 2 * pi * dfreq

exp_Zd = 2*R
dexp_Zd = 2 * dR
exp_Zs = R - 1j / (w_exp * C1) + (1/R + 1j*w_exp*C3)**-1
dexp_Zs = np.sqrt(
  ((1 + (1 + 1j*w_exp*C3*R)**-2) * dR)**2 +
  (1j / (w_exp*C1**2) * dC1)**2 +
  (R**2*1j*w_exp / (1 + 1j*w_exp*C3*R)**2 * dC3)**2 +
  ((1j / (w_exp**2*C1) + 1j*C3*R**2 / (1 + 1j*w_exp*C3*R)) * dw_exp)**2
)

exp_Id = vin / exp_Zd
dexp_Id = np.sqrt((dvin/exp_Zd * dvin)**2 + (vin/exp_Zd**2 * dexp_Zd)**2)
exp_Is = vin / exp_Zs
dexp_Is = np.sqrt((dvin/exp_Zs * dvin)**2 + (vin/exp_Zs**2 * dexp_Zs)**2)
print((dvin/exp_Zs * dvin), (vin/exp_Zs**2 * dexp_Zs))

exp_V2 = vin - R*exp_Id
dexp_V2 = np.sqrt(dvin**2 + (exp_Id*dR)**2 + (R*dexp_Id)**2)
exp_V1 = vin - (R - 1j / (w_exp * C1)) * exp_Is
dexp_V1 = np.sqrt(dvin**2 + (R - 1j/(w_exp * C1))**2*dexp_Is**2 +
    (exp_Is*dR)**2 + (1j*exp_Is*dw_exp/(w_exp**2**C1))**2 + (1j*exp_Is*dC1/(w_exp*C1**2))**2)

A = np.abs(exp_V1)
dA = dexp_V1

diff_ph = np.log((exp_V2 - A*np.exp(1j*ph)) / vout) / 1j * 180 / pi
P = (vout / (exp_V2 - A*np.exp(1j*ph)))**2
ddiff_ph = 180/(pi*1j) * P * np.sqrt((dexp_V2/vout)**2 + (np.exp(1j*ph)*dA/vout)**2 +
    (A*1j*np.exp(1j*ph)*dph/vout)**2 + ((exp_V2 - A*np.exp(1j*ph))/vout**2*dvout)**2)

########## ANDAMENTI TEORICI #########################################
f = np.logspace(1, 6, num=500)
w = 2 * pi * f

Zd = 2*R
Zs = R - 1j / (w * C1) + (1/R + 1j*w*C3)**-1

Id = vin / Zd
Is = vin / Zs

V2 = vin - R*Id
V1 = vin - (R - 1j / (w * C1)) * Is

dV = V1 - V2
tV = np.abs(dV)
tph = arg(V2 - V1) * 180 / pi

tdB = 20 * np.log10(tV/vin)

#A = (w * R * C1)**2
#rV = np.sqrt(A**4 + 6*A**3 - 5*A**2 + 6*A + 1) / (2*A**2 + 14*A + 2)
#adB = 20 * np.log10(rV)

#### CORREZIONE
F = 30

corr_Zd = 2*R
corr_Zs = R - 1j / (w * C1) + (1/R + (F - 1j/(w*C3))**-1)**-1

corr_Id = vin / corr_Zd
corr_Is = vin / corr_Zs

corr_V2 = vin - R*corr_Id
corr_V1 = vin - (R - 1j / (w * C1)) * corr_Is

corr_dV = corr_V1 - corr_V2
corr_tV = np.abs(corr_dV)
corr_tph = arg(corr_V2 - corr_V1) * 180 / pi

corr_tdB = 20 * np.log10(corr_tV/vin)

############### GRAFICO ###################################
matplotlib.rcParams['font.size'] = 15

### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(9.5, 10), dpi=65)

# Titolo del grafico
f1.suptitle("Filtro notch con ponte di Wien",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(2, 1, 1)

# crea plot con le barre d'errore (o anche senza)
line = ax1.errorbar(x=f, y=tdB,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3,
    zorder=1)

line2 = ax1.errorbar(x=f, y=corr_tdB,
    #yerr=dy, #xerr=,
    fmt='--', c='black', linewidth=2,
    zorder=1)

dots1 = ax1.errorbar(x=freq, y=dB,
    yerr=ddB, #xerr=,
    fmt='o', c="white",
    markersize=7, markeredgewidth=1,
    ecolor='black', elinewidth=4,
    capsize=0, zorder=2)
    
ax1.set_ylabel(u'Attenuazione [dB]',
    labelpad=12, fontsize=16)


ax1.grid(True)
ax1.set_xscale('log')
ax1.set_ylim((-17, -5))
ax1.set_xlim((40, 1.2e5))
for label in ax1.get_xaxis().get_majorticklabels():
  label.set_visible(False)
#ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))

# GRAFICO 2
ax2 = f1.add_subplot(2, 1, 2)

# crea plot con le barre d'errore (o anche senza)
line2 = ax2.errorbar(x=f, y=tph,
    #yerr=dy, #xerr=,
    fmt='-', c='gray', linewidth=3)

line2_corr = ax2.errorbar(x=f, y=corr_tph,
    #yerr=dy, #xerr=,
    fmt='--', c='black', linewidth=2)

dots2 = ax2.errorbar(x=freq, y=diff_ph,
    yerr=ddiff_ph, #xerr=,
    fmt='o', c='white', ecolor='black',
    markersize=7, markeredgewidth=1,
    elinewidth=2, capsize=0, zorder=2)

ax2.set_xlabel(u'Frequenza [Hz]',
    labelpad=12, fontsize=16)
ax2.set_ylabel(u'Sfasamento [gradi]',
    labelpad=12, fontsize=16)


ax2.grid(True)
ax2.set_xscale('log')
ax2.set_ylim((-35, 35))
ax2.set_xlim((40, 1.2e5))
#ax2.set_yticks((-90, -67.5, -45, -22.5, 0, 22.5, 45, 67.5, 90))

# questo produce una legenda
#ax2.legend((dots1, line, line_corr), ("Punti sperimentali", "Previsione teorica", "Correzione"), 'upper right',
#    prop={'size': 15})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.12, right=0.97,
    top=0.92, bottom=0.09, hspace=0.08, wspace=0)

# mostra grafico
plt.show()  
