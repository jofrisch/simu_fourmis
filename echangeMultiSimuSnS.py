# coding:utf-8
"""Pour lancer la simulation dans le terminal: for ii in `seq 20`; do python echangeSim.py $ii ; done


 for ii in `seq 10`; do for jj in `seq 5`; do python nimp.py $ii $jj; done; done
""" 


from random import *
from math import *

import numpy as np
from sys import argv

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

def evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit):
	
    individusAleatoires = range(NbIndividus)
    
    res = []
    res.append(TableauFourmis)
		
    for temps in range(NbSimul):

        np.random.shuffle(individusAleatoires)
        
        for i in xrange(NbIndividus/2):
            k = individusAleatoires[2*i]
            l = individusAleatoires[2*i+1]
            
            ChargePremier = TableauFourmis[k]
            ChargeSecond = TableauFourmis[l]

            x = random()
            y = random()

            if x<ProbaRecevoir(ChargePremier) and y > ProbaRecevoir(ChargeSecond):
                don = + ChargeUnit
            elif x>ProbaRecevoir(ChargePremier) and y < ProbaRecevoir(ChargeSecond):
                don = - ChargeUnit
            else:
                don=0
            
            TableauFourmis[k] = TableauFourmis[k]+don
            TableauFourmis[l] = TableauFourmis[l]-don

        res.append(TableauFourmis)
    return res


######## TableauFourmis #######

TableauFourmis = [0 for i in range(NbIndividus)]

######## Conditions initiales ########

CI=[(c_moyenne,NbIndividus)]
#On impose les CI:
palier=0
for element in CI:
    j=0
    while j<element[1]:
        TableauFourmis[palier+j]=element[0]
        j+=1
    palier += j


##### Main #####

data = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit)


####### Ecriture du tableau dans un fichier #######
tf = np.array(data)[-1,:]

np.savetxt('newData/donneesLin/10000fourmis/cmoyenne_%i/snapshot500_%02i_charge_%02i.txt' % (c_moyenne,numero,c_moyenne,), tf)


print "hey bro!" 


