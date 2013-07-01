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
    'figure.subplot.wspace' : 0.1
    }
plt.rcParams.update(params)



pasDeTemps = 5000

tableau_charges = [10,25,35,50,65,75]

indice = 0


for charge in tableau_charges:
	
	subp = plt.subplot(321+indice)
	

	for i in range(1,9):
		
		evolution_std = np.loadtxt('pre_equilibre/Cste/std_%02ipdt_%02i_charge_%02i.txt' % (pasDeTemps,i,charge))
		evolution_std_tmp = evolution_std - evolution_std[4500]
		evolution_std_best = evolution_std_tmp/evolution_std_tmp[0]
		
		plt.plot(np.arange(pasDeTemps+1),evolution_std_best)


	plt.legend(loc="upper left")
	if indice in [0,2,4]: 
		plt.ylabel(u"Ecart type")
	if indice in [4,5]:
		plt.xlabel(u"Temps")

		
	
	indice += 1



plt.show()

