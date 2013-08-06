import numpy as np
import matplotlib.pyplot as plt

from glob import glob

import argparse

parser = argparse.ArgumentParser(description='Analyze m2 data from the simulation.')
parser.add_argument('-q', type=int, help='Average load', nargs='+')
parser.add_argument('--mean', action='store_true', help='Plot only the mean for a given charge')
parser.add_argument('--law', type=str, choices=['cste', 'lin', 'anti', 'vague' ], help='Probability exchange law', default='cste')
parser.add_argument('--asyn_steps', type=int, help='Number of time steps for asynchronous simulation', default=-1)

args = parser.parse_args()

charges = args.q

cc = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for c in charges:
    runs = glob('ComparaisonSYAS/m2_sync%02i_%s_*_N500_Q%02i.txt' % (args.asyn_steps ,args.law,c,))
    m2 = []
    col = cc.pop(0)
    label = False
    for r in runs:
        if args.mean:
            m2.append(np.loadtxt(r))
        else:
            if not label:
                plt.plot(np.loadtxt(r), label='Charge %02i' % (c,), c=col)
                label = True
            else:
                plt.plot(np.loadtxt(r), c=col)
    if args.mean:
        m2 = np.array(m2)
        plt.plot(m2.mean(axis=0), label='Charge %02i' % (c,))

plt.legend()
plt.show()
