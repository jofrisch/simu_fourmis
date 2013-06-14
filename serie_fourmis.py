# coding:utf-8
"""Pour lancer la simulation dans le terminal: for ii in `seq 20`; do python echangeSim.py $ii ; done


 for ii in `seq 10`; do for jj in `seq 5`; do python nimp.py $ii $jj; done; done
""" 


from random import *
from math import *

import numpy as np
from sys import argv
from evolution import *


c_moyenne = int(argv[1])
numero = int(argv[2])

####### Paramètres ########
NbSimul = 500

NbIndividus = 10000 #Choisir un nb pair
capaciteStock = 100
ChargeUnit = 1



####### Loi de proba #######

def ProbaRecevoir(charge,capaciteStock):
    if 0<charge<capaciteStock :
        return 1-1.*charge/capaciteStock
    elif charge == 0:
        return 1
    else:
		return 0



###### Evolution de population #####
"""
def evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit):
	
	
    individusAleatoires = range(NbIndividus)
    
    Xrandom = []
    for j in range(NbIndividus):
		Xrandom.append(random())
		
    for temps in range(NbSimul):

        shuffle(individusAleatoires)
        shuffle(Xrandom)
        
        i=0
        
        while i < NbIndividus/2:
            k = individusAleatoires[2*i]
            l = individusAleatoires[2*i+1]
            
            ChargePremier = TableauFourmis[k][temps]
            ChargeSecond = TableauFourmis[l][temps]

            x = Xrandom[2*i]
            y = Xrandom[2*i+1]

            if x<ProbaRecevoir(ChargePremier,capaciteStock) and y > ProbaRecevoir(ChargeSecond,capaciteStock):
                don = + ChargeUnit
            elif x>ProbaRecevoir(ChargePremier,capaciteStock) and y < ProbaRecevoir(ChargeSecond,capaciteStock):
                don = - ChargeUnit
            else:
                don=0
            
            TableauFourmis[k][temps+1] = TableauFourmis[k][temps]+don
            TableauFourmis[l][temps+1] = TableauFourmis[l][temps]-don
	    i+=1
"""


######## TableauFourmis #######
"""
TableauFourmis= [0]*NbIndividus
for i in range(NbIndividus):
    TableauFourmis[i]=[0]*(NbSimul+1) # on considère le tps de 0 jusque NbSimul
"""
TableauFourmis = np.zeros((NbIndividus,), dtype=np.int64)


######## Conditions initiales ########
intervals_init = [1,2,5,10,20,25,50,100] #8 distributions initiales différentes / 8 simulations différentes
for i in range(c_moyenne*(NbIndividus/intervals_init[numero-1])):
	fourmis = randint(0,NbIndividus-1)
	while TableauFourmis[fourmis] > 99:
		fourmis = randint(0,NbIndividus-1)
	TableauFourmis[fourmis] += intervals_init[numero-1]

##### Main #####
data = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit)



####### Ecriture du tableau dans un fichier #######
table_std = np.array(data).std(axis=1)
print table_std
#np.savetxt('pre_equilibre/Anti/std_%02ipdt_%02i_charge_%02i.txt' % (NbSimul,numero,c_moyenne), table_std)

print "Done!" 


