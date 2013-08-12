import numpy as np
import matplotlib.pyplot as plt

from glob import glob

import argparse

parser = argparse.ArgumentParser(description='Analyze m2 data from the simulation.')
parser.add_argument('-q', type=int, help='Average load', default=20)
parser.add_argument('--mean', action='store_true', help='Plot only the mean for a given charge')
parser.add_argument('--law', type=str, choices=['cste', 'lin', 'anti', 'vague' ], help='Probability exchange law', default='cste')
parser.add_argument('--asyn_steps', type=int, help='Number of time steps for asynchronous simulation', default=250)
parser.add_argument('--steps_max', type=int, help='Length of datas', default=2000)

args = parser.parse_args()


cc = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

runsSY = glob('ComparaisonSYAS/m2_sync-1_%s_*_N500_Q%02i.txt' % (args.law,args.q,))
runsAS = glob('ComparaisonSYAS/m2_sync%02i_%s_*_N500_Q%02i.txt' % (args.asyn_steps ,args.law,args.q,))

m2SY = []
m2AS = []
col = cc.pop(0)	

label = False

for r in runsAS:
    m2AS.append(np.loadtxt(r)[:args.steps_max])

for r in runsSY:
    m2SY.append(np.loadtxt(r)[:args.steps_max])

plt.plot(np.array(m2SY).mean(axis=0), label='Simulation sychrone')
plt.plot(np.array(m2AS).mean(axis=0), label='Simulation asynchrone')

plt.legend(loc="lower right")
plt.show()
