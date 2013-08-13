import numpy as np
import matplotlib.pyplot as plt

from glob import glob
import os.path

import argparse

parser = argparse.ArgumentParser(description='Analyze m2 data from the simulation.')
parser.add_argument('-q', type=int, help='Average load', default=20)
parser.add_argument('-N', type=int, help='Number of individuals', default=500)
parser.add_argument('--law', type=str, choices=['cste', 'lin', 'anti', 'vague' ], help='Probability exchange law', default='cste')
parser.add_argument('--asyn_steps', type=int, help='Number of time steps for asynchronous simulation', default=250)

args = parser.parse_args()

cc = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

runsSY = glob(os.path.join('ComparaisonSYAS', 'm2_*_%s_sync-001_N%02i_Q%02i.txt' % (args.law,args.N,args.q)))
runsAS = glob(os.path.join('ComparaisonSYAS', 'm2_*_%s_sync%04i_N%02i_Q%02i.txt' % (args.law,args.asyn_steps,args.N,args.q)))

m2SY = []
m2AS = []

for r in runsAS:
    m2AS.append(np.loadtxt(r))

for r in runsSY:
    m2SY.append(np.loadtxt(r))

m2SY = np.array(m2SY)
m2AS = np.array(m2AS)

col = cc.pop(0)
m = m2SY.mean(axis=0)
s = m2SY.std(axis=0)
plt.plot(m, label='Simulation synchrone', c=col)
plt.plot(m+s, c=col, ls=':')
plt.plot(m-s, c=col, ls=':')

col = cc.pop(0)
m = m2AS.mean(axis=0)
s = m2AS.std(axis=0)
plt.plot(m, label='Simulation asynchrone', c=col)
plt.plot(m+s, c=col, ls=':')
plt.plot(m-s, c=col, ls=':')

plt.legend(loc="lower right")
plt.show()
