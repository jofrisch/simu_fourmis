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
import os.path

import h5py

parser = argparse.ArgumentParser(description='Run a simulation of food exchange.')
parser.add_argument('id', type=int, help='id of the simulation')
parser.add_argument('name', type=str, help='name of the simulation directory')
parser.add_argument('-q', type=int, help='Average load', required=True)
parser.add_argument('-N', type=int, help='Number of individuals', default=500)
parser.add_argument('--qmax', type=int, help='Capacity of the individuals', default=100)
parser.add_argument('--steps', type=int, help='Number of time steps', default=1000)
parser.add_argument('--asyn_steps', type=int, help='Number of time steps for asynchronous simulation', default=-1)
parser.add_argument('--law', type=str, choices=['cste', 'lin', 'anti', 'vague' ], help='Probability exchange law', default='cste')
parser.add_argument('--exch', type=int, help='Average inverse exchanged quantity', default=100)
parser.add_argument('--charge_distrib', type=int, help='Elementary charge for initial distribution', default=1)

parser.add_argument('--h5_out', type=str, help='HDF5 filename for outputting trajectory', default='')

args = parser.parse_args()

if not os.path.isdir(args.name):
    print "No directory of name ", args.name
    exit()

c_moyenne = args.q
numero = args.id

num_law = {'cste':0, 'lin':1, 'anti':2, 'vague':3,'applatie':4}

####### Paramètres ########
NbSimul = args.steps

NbIndividus = args.N
if NbIndividus%2 !=0:
    print 'the number of individuals should be even'
    exit()
capaciteStock = args.qmax
ChargeUnit = 1

######## TableauFourmis #######

TableauFourmis = np.zeros((NbIndividus,), dtype=np.int64)
######## Conditions initiales ########
echange.distribute_multi(TableauFourmis, c_moyenne, capaciteStock,args.charge_distrib)
##### Main #####

if len(args.h5_out)>0:
    f = h5py.File(args.h5_out)
else:
    f = None

data, m2 = evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit,num_law[args.law], args.exch, f, args.asyn_steps)

if f:
    f.close()

####### Ecriture du tableau dans un fichier #######
tf = np.array(data)

np.savetxt(os.path.join(args.name,'m2_%02i_%s_sync%04i_N%02i_Q%02i_ex%05i.txt' % (numero,args.law,args.asyn_steps,NbIndividus,c_moyenne,args.exch)), np.array(m2)/capaciteStock**2)
np.savetxt(os.path.join(args.name,'snapshot_%02i_%s_sync%04i_N%02i_Q%02i_ex%05i_Steps%i.txt'%(numero,args.law,args.asyn_steps,NbIndividus,c_moyenne,args.exch,args.steps)),tf[-1])

print "hey bro!"


