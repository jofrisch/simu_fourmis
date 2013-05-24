# coding:utf-8
"""Pour lancer la simulation dans le terminal: for ii in `seq 20`; do python echangeSim.py $ii ; done


 for ii in `seq 10`; do for jj in `seq 5`; do python nimp.py $ii $jj; done; done
""" 


from random import *
from math import *

import numpy as np
from sys import argv


c_moyenne = int(argv[1])
numero = int(argv[2])

####### Paramètres ########
NbSimul = 500

NbIndividus = 10000 #Choisir un nb pair
capaciteStock = 100
ChargeUnit = 1



####### Loi de proba #######

def ProbaRecevoir(charge,capaciteStock):
    l = charge * 1. / capaciteStock
    if 0<l<1 :
        resultat = 1-l
    elif l == 0:
        resultat = 1
    else:
		resultat = 0

    return resultat



###### Evolution de population #####

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



######## TableauFourmis #######

TableauFourmis= [0]*NbIndividus
for i in range(NbIndividus):
    TableauFourmis[i]=[0]*(NbSimul+1) # on considère le tps de 0 jusque NbSimul


######## Conditions initiales ########

CI=[(c_moyenne,NbIndividus)]
#On impose les CI:
palier=0
for element in CI:
    j=0
    while j<element[1]:
        TableauFourmis[palier+j][0]=element[0]
        j+=1
    palier += j


##### Main #####

evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit)



####### Ecriture du tableau dans un fichier #######
tf = np.array(TableauFourmis)[:,-1]

np.savetxt('newData/donneesLin/10000fourmis/cmoyenne_%i/snapshot500_%02i_charge_%02i.txt' % (c_moyenne,numero,c_moyenne,), tf)


print "hey bro!" 


