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
NbSimul = 50

NbIndividus = 50 #Choisir un nb pair
capaciteStock = 100
ChargeUnit = 1


######## TableauFourmis #######

TableauFourmis = np.zeros((NbIndividus,), dtype=np.int64)


######## Conditions initiales ########
intervals_init = [1,2,5,10,20,25,50,100] #8 distributions initiales différentes / 8 simulations différentes

for i in range(c_moyenne*(NbIndividus/intervals_init[numero-1])):
	while True:
		fourmis = randint(0,NbIndividus-1)
		if TableauFourmis[fourmis]+intervals_init[numero-1] <= capaciteStock:
			TableauFourmis[fourmis]+= intervals_init[numero-1]
			break

##### Main #####
data = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit)



####### Ecriture du tableau dans un fichier #######
table_std = np.array(data).std(axis=1)
print data[7]-data[8]
#np.savetxt('std_%02ipdt_%02i_charge_%02i.txt' % (NbSimul,numero,c_moyenne), table_std)

print "Done!" 


