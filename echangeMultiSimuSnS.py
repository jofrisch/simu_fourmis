# coding:utf-8
"""Pour lancer la simulation dans le terminal: for ii in `seq 20`; do python echangeSim.py $ii ; done


 for ii in `seq 10`; do for jj in `seq 5`; do python nimp.py $ii $jj; done; done
""" 

from random import *
from math import *

import numpy as np
from sys import argv

import echange
from evolution import evolution

if len(argv)<3:
    print """Usage:
python echangeMultiSimuSnS.py c_moyenne numero
où c_moyenne est la charge moyenne par fourmi (entier entre 1 et 100) et numero
une référence arbitraire pour éxécuter plusieurs fois la même simulation."""


c_moyenne = int(argv[1])
numero = int(argv[2])

####### Paramètres ########
NbSimul = 500

NbIndividus = 10000 #Choisir un nb pair
capaciteStock = 100
ChargeUnit = 1



####### Loi de proba #######

def ProbaRecevoir(charge):
    return 1.-charge*1./capaciteStock

###### Evolution de population #####

def one_step(individusAleatoires, TableauFourmis, PR):
    NbIndividus = len(TableauFourmis)
    for i in xrange(NbIndividus/2):
        k = individusAleatoires[2*i]
        l = individusAleatoires[2*i+1]

        ChargePremier = TableauFourmis[k]
        ChargeSecond = TableauFourmis[l]

        x = random()
        y = random()

        if x<PR(ChargePremier) and y > PR(ChargeSecond):
            don = 1
        elif x>PR(ChargePremier) and y < PR(ChargeSecond):
            don = -1
        else:
            don=0

        TableauFourmis[k] = TableauFourmis[k]+don
        TableauFourmis[l] = TableauFourmis[l]-don

######## TableauFourmis #######

TableauFourmis = np.zeros((NbIndividus,), dtype=np.int64)

######## Conditions initiales ########

echange.distribute(TableauFourmis, c_moyenne, capaciteStock)

##### Main #####

data = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit)


####### Ecriture du tableau dans un fichier #######
tf = np.array(data)[-1,:]

np.savetxt('snapshot500_%02i_charge_%02i.txt' % (numero,c_moyenne,), tf)


print "hey bro!" 


