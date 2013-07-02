# coding:utf-8
"""Pour lancer la simulation dans le terminal: for ii in `seq 20`; do python echangeSim.py $ii ; done


 for ii in `seq 10`; do for jj in `seq 5`; do python nimp.py $ii $jj; done; done
""" 

from random import *
from math import *

import numpy as np

import echange
from evolution import evolution
import argparse

parser = argparse.ArgumentParser(description='Run a simulation of food exchange.')
parser.add_argument('id', type=int, help='id of the simulation')
parser.add_argument('-q', type=int, help='Average load', required=True)
parser.add_argument('-N', type=int, help='Number of individuals', default=500)
parser.add_argument('--qmax', type=int, help='Capacity of the individuals', default=100)
parser.add_argument('--steps', type=int, help='Number of time steps', default=1000)
parser.add_argument('--law', type=str, choices=['cste', 'lin', 'anti', 'vague' ], help='Probability exchange law', default='cste')

args = parser.parse_args()

c_moyenne = args.q
numero = args.id

num_law = {'cste':0, 'lin':1, 'anti':2, 'vague':3}

####### Paramètres ########
NbSimul = args.steps

NbIndividus = args.N
if NbIndividus%2 !=0:
    print 'the number of individuals should be even'
    exit()
capaciteStock = args.qmax
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

data = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit,num_law[args.law])


####### Ecriture du tableau dans un fichier #######
tf = np.array(data)[-1,:]

np.savetxt('snapshot%05i_%02i_charge_%02i.txt' % (NbSimul,numero,c_moyenne,), tf)


print "hey bro!" 


