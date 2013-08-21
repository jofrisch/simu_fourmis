# coding: utf-8

from random import *
from math import *

from scipy.optimize import brentq, leastsq

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


def f(r, Q, N):
	return charge(r,N)-Q
	
def plot_distribution(Q,N):
	
	tableg = gg(N)
	r = brentq(f,0.01,10, args=(Q,N))
	
	l = np.arange(N+1)
	Xl_tmp = np.array([1]+[r**i * tableg[i-1] for i in range(1,N+1)])
	Xl = X0(r,N)*Xl_tmp
	plt.plot(l,Xl)

	print Xl.sum(), r, r/(1.+r)
        fitfunc = lambda p, x: p[0]*np.exp(-(x-p[1])**2/(2*p[2]**2))
        errfunc = lambda p, x, y: (fitfunc(p, x) - y)
        p1, success = leastsq(errfunc, [1., N/2, N/2], args=(l, Xl))
        print p1[2], p1[2]/np.sqrt(1.*N)


def MonHistogram(liste,UnitCharge,capaciteStock):
    histo = [0]*(capaciteStock/UnitCharge+1)
    for element in liste:
        indice = int(element/UnitCharge)
        histo[indice]+=1
    return histo


#####################################


UnitCharge=1
capaciteStock=10

tableau_charges = [1,2,3,5,6,7]

indice = 0
for charge_value in tableau_charges:

	plt.subplot(321+indice) ; indice += 1
        print "############ Q = ", charge_value
	plot_distribution(charge_value, capaciteStock)
	plot_distribution(charge_value*5, capaciteStock*5)
	plot_distribution(charge_value*10, capaciteStock*10)
	plot_distribution(charge_value*20, capaciteStock*20)


plt.show()

