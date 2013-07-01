# coding: utf-8

from random import *
from math import *

from scipy.optimize import brentq

import numpy as np
from sys import argv

import matplotlib.pyplot as plt


########################################



def PR(i,N):
	if i == 0:
		resultat = 1.
	elif i == N:
		resultat = 0.
	else:
		l = 1.*i/N
		resultat =  1-l
	return resultat
	
def PD(i,N):
	return 1-PR(i,N)

def X0(r,N):
	tableg = gg(N)
	table_tmp = [1]

	for i in range(1,N+1):
		table_tmp.append(r**i*tableg[i-1])
	return 1/sum(table_tmp)

def charge(r,N):
	tableg=gg(N)
	valeur_interm = [0]
	for i in range(1,N+1):
		valeur_interm.append(i*r**i*tableg[i-1])
	return X0(r,N)*sum(valeur_interm)
	
def gg(N):
	table_f = []
	for i in range(N):
		table_f.append(1.*PR(i,N)/PD(i+1,N))
	return np.cumprod(table_f)


def f(r, q):
	return charge(r,100)-q
	
def plot_distribution(Q,N):
	
	tableg = gg(N)
	r = brentq(f,0.01,10, args=(Q,))
	
	l = np.arange(N+1)
	Xl_tmp = np.array([1]+[r**i * tableg[i-1] for i in range(1,N+1)])
	Xl = X0(r,N)*Xl_tmp
	plt.plot(l,Xl)

	print Xl.sum()


def MonHistogram(liste,UnitCharge,capaciteStock):
    histo = [0]*(capaciteStock/UnitCharge+1)
    for element in liste:
        indice = int(element/UnitCharge)
        histo[indice]+=1
    return histo


#####################################


UnitCharge=1
capaciteStock=100


tableau_charges = [10,25,35,50,65,75]

superTableau= [0]*len(tableau_charges)
superMoyenne = [0]*len(tableau_charges)

indice = 0

correspondance = [15000,30000,15000,45000,750,750]

for charge_value in tableau_charges:
	superTableau[indice] = []

	for i in range(1,11):
		histo = MonHistogram(np.loadtxt('newData/donneesLin/10000fourmis/cmoyenne_%02i/snapshot500_%02i_charge_%02i.txt' % (charge_value,i,charge_value)),1,100)
		superTableau[indice].append(histo)

	superTableau[indice] = np.array(superTableau[indice])
	superMoyenne[indice] = np.mean(superTableau[indice],axis=0)

	plt.subplot(321+indice)
	plt.plot(np.arange(0,capaciteStock+1,UnitCharge),superMoyenne[indice]/10000,'k-',label="%02i"%(charge_value,))
	plot_distribution(charge_value, capaciteStock)

	
	plt.legend(loc="upper center")
	if indice in [0,2,4]: 
		plt.ylabel(u"Nb individus")
	if indice in [5,6]:
		plt.xlabel(u"Charge transportée")

		
	
	indice += 1







#plt.title("Distribution moyennee apres %d pas de temps.")
#plt.xlabel(u"Charge transportee (en % de la capacite maximale)")
#plt.legend(("C.I. 1", "C.I. 2", "C.I. 3"),loc="upper right")
plt.show()

