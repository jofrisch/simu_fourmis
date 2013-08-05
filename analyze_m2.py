import numpy as np
import matplotlib.pyplot as plt

from glob import glob

import argparse

parser = argparse.ArgumentParser(description='Analyze m2 data from the simulation.')
parser.add_argument('-q', type=int, help='Average load', nargs='+')
parser.add_argument('--mean', action='store_true', help='Plot only the mean for a given charge')
args = parser.parse_args()

charges = args.q

cc = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for c in charges:
    runs = glob('m2_*_charge_%02i.txt' % (c,))
    m2 = []
    col = cc.pop(0)
    for r in runs:
        if args.mean:
            m2.append(np.loadtxt(r))
        else:
            plt.plot(np.loadtxt(r), label='Charge %02i' % (c,), c=col)
    if args.mean:
        m2 = np.array(m2)
        plt.plot(m2.mean(axis=0), label='Charge %02i' % (c,))

plt.legend()
plt.show()
