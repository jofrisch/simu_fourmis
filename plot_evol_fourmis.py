# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from sys import argv


myp = { 'l' : 0.22, 'w' : 0.7, 'b' : 0.2, 'h' : 0.7, 'size': [5,3.5]}
params = {
    'axes.labelsize' : 20,
    'axes.titlesize' : 20,
    'legend.fontsize' : 14,
    'xtick.labelsize' : 14,
    'xtick.major.pad' : 8,
    'ytick.labelsize' : 14,
    'ytick.major.pad' : 8,
    'figure.figsize' : myp['size'],
    'figure.subplot.left' : myp['l'],
    'figure.subplot.right' : myp['l']+myp['w'],
    'figure.subplot.bottom' : myp['b'],
    'figure.subplot.top' : myp['b']+myp['h'],
    'figure.subplot.hspace' : 0.4,
    'figure.subplot.wspace' : 0.
    }
plt.rcParams.update(params)

UnitCharge=1
capaciteStock=100

charge = int(argv[1])
nb_fourmis = int(argv[2])

tau = 500

tableauFourmis = np.loadtxt('pre_equilibre/Anti/tableau250Fourmis_charge_%02i_interval_00_5000.txt' % (charge))[:,-tau:]


t = np.arange(tau)

for fourmis in range(nb_fourmis):
	
	plt.plot(t,tableauFourmis[fourmis],'-')


plt.ylabel(u"Charge")
plt.xlabel(u"Temps")

print 'hello'
plt.savefig('pre_equilibre/Anti/Evolution%02ifourmisEquilibre/evolution_%02ifourmis_charge%02i.pdf'%(nb_fourmis,nb_fourmis,charge))

