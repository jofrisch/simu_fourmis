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
NbSimul = 5000

NbIndividus = 10000 #Choisir un nb pair
capaciteStock = 100
ChargeUnit = 1



####### Loi de proba #######

def ProbaRecevoir(charge,capaciteStock):
    l = charge * 1. / capaciteStock
    if 0<l<1 :
        return -2*l**2+1.5*l+0.5
    elif l == 0:
        return 1
    else:
		return 0



######## Conditions initiales ########
TableauFourmis = np.loadtxt('newData/donneesVague/10000fourmis/snapshot5000_%02i_charge_%02i.txt' % (numero,c_moyenne))


##### Main #####

datas = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit)



####### Ecriture du tableau dans un fichier #######

np.savetxt('newData/donneesVague/10000fourmis/snapshot5000_%02i_charge_%02i.txt' % (numero,c_moyenne,), np.array(datas)[:,-1])


print "Done!" 


