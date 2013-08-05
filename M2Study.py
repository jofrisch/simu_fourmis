# coding:utf-8
"""Pour lancer la simulation dans le terminal: for ii in `seq 20`; do python echangeSim.py $ii ; done


 for ii in `seq 10`; do for jj in `seq 5`; do python nimp.py $ii $jj; done; done
""" 


from random import *
from math import *

import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Run a simulation of food exchange.')
parser.add_argument('id', type=int, help='id of the simulation')
parser.add_argument('-q', type=int, help='Average load', required=True)
parser.add_argument('-N', type=int, help='Number of individuals', default=500)
parser.add_argument('--qmax', type=int, help='Capacity of the individuals', default=100)
parser.add_argument('--steps', type=int, help='Number of time steps', default=1000)
parser.add_argument('--steps_as', type=int, help='Number of time steps for asynchronous simulation', default=1000)
parser.add_argument('--law', type=str, choices=['cste', 'lin', 'anti', 'vague' ], help='Probability exchange law', default='cste')

args = parser.parse_args()

c_moyenne = args.q
numero = args.id

####### Paramètres ########
NbSimul_SY = args.steps
NbSimul_AS = args.steps_as

NbIndividus = args.N
if NbIndividus%2 !=0:
    print 'the number of individuals should be even'
    exit()
capaciteStock = args.qmax
ChargeUnit = 1



####### Loi de proba #######

def ProbaRecevoir(charge):
	return 1-charge*1./capaciteStock
"""
	l = 1./capaciteStock*charge
	if 0<charge<capaciteStock:
		return -2*l**2+1.5*l+0.5
	elif charge == 0:
		return 1
	elif charge == capaciteStock:
		return 0"""

###### Evolution de population #####

def evolution_AS(TableauFourmis_AS,NbSimul,NbIndividus,capaciteStock,ChargeUnit):
	
    M2Table = []
		
    for temps in range(NbSimul):


        k = np.random.randint(NbIndividus)
        l = np.random.randint(NbIndividus)
        while k==l:
		    l = np.random.randint(NbIndividus)
			
        ChargePremier = TableauFourmis_AS[k]
        ChargeSecond = TableauFourmis_AS[l]

        x = random()
        y = random()

        if x<ProbaRecevoir(ChargePremier) and y > ProbaRecevoir(ChargeSecond):
            don = + ChargeUnit
        elif x>ProbaRecevoir(ChargePremier) and y < ProbaRecevoir(ChargeSecond):
            don = - ChargeUnit
        else:
            don=0
            
        TableauFourmis_AS[k] = TableauFourmis_AS[k]+don
        TableauFourmis_AS[l] = TableauFourmis_AS[l]-don
        
        M2 = 0
        for charge in TableauFourmis_AS:
            M2 += charge**2
        M2Table.append(M2)
        
    return M2Table


def evolution_SY(TableauFourmis_SY,NbSimul,NbIndividus,capaciteStock,ChargeUnit):
		
    M2Table = []
	
    indices = np.arange(NbIndividus)
	
    for temps in range(NbSimul):


        np.random.shuffle(indices)
		
		
        for i in range(NbIndividus/2):	
            k=indices[2*i]
            l=indices[2*i+1]
        
            ChargePremier = TableauFourmis_SY[k]
            ChargeSecond = TableauFourmis_SY[l]

            x = random()
            y = random()

            if x<ProbaRecevoir(ChargePremier) and y > ProbaRecevoir(ChargeSecond):
                don = + ChargeUnit
            elif x>ProbaRecevoir(ChargePremier) and y < ProbaRecevoir(ChargeSecond):
                don = - ChargeUnit
            else:
                don=0
            
            TableauFourmis_SY[k] = TableauFourmis_SY[k]+don
            TableauFourmis_SY[l] = TableauFourmis_SY[l]-don
        
        M2 = 0
        for charge in TableauFourmis_AS:
            M2 += charge**2
        M2Table.append(M2)

        
    return M2Table

######## TableauInit #######

TableauInit = [0 for i in range(NbIndividus)]

######## Conditions initiales ########
for element in range(c_moyenne*NbIndividus):
    while True:
        fourmi = np.random.randint(0,NbIndividus)
        if TableauInit[fourmi]<capaciteStock:
            TableauInit[fourmi]+=1
            break


##### Main #####
print "start AS"
TableauFourmis_AS = TableauInit
M2_AS = evolution_AS(TableauFourmis_AS,NbSimul_AS,NbIndividus,capaciteStock,ChargeUnit)

print "start SY"
TableauFourmis_SY = TableauInit
M2_SY = evolution_SY(TableauFourmis_SY,NbSimul_SY,NbIndividus,capaciteStock,ChargeUnit)

####### Ecriture du tableau dans un fichier #######


np.savetxt('M2study/M2AS_Lineaire_%02i_Q%02i.txt' % (numero,c_moyenne,), np.array(M2_AS))
np.savetxt('M2study/M2SY_Lineaire_%02i_Q%02i.txt' % (numero,c_moyenne,), np.array(M2_SY))


print "Done!"


