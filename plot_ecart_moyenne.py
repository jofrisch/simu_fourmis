# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
from sys import argv




def MonHistogram(liste,UnitCharge,capaciteStock):
    histo = [0]*(capaciteStock/UnitCharge+1)
    for element in liste:
        indice = int(element/UnitCharge)
        histo[indice]+=1
    return histo

UnitCharge=1
capaciteStock=100

tableau_charges = [10,25,35,50,65,75]
interval = (0,5000)
nb_fourmis = 250

indice = 0
for charge in tableau_charges:
	tableauFourmis = np.loadtxt('pre_equilibre/Anti/tableau250Fourmis_charge_%02i_interval_%02i_%02i.txt' % (charge,interval[0],interval[1]))

	liste_histogrammes = []
	
	for i in range(nb_fourmis):
		liste_histogrammes.append(MonHistogram(tableauFourmis[i,:],UnitCharge,capaciteStock))


	moyenne = np.array(liste_histogrammes).mean(axis=0)
	ecart_type = np.array(liste_histogrammes).std(axis=0)


	plt.subplot(321+indice)
	
	plt.plot(np.arange(101),moyenne)
	plt.plot(np.arange(101),moyenne+ecart_type)
	plt.plot(np.arange(101),moyenne-ecart_type)
	
	if indice in [0,2,4]:
		plt.ylabel(u"Fréquence")
	if indice in [5,6]:
		plt.xlabel(u"Charge")
	
	
	indice += 1


plt.show()

