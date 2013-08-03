# coding:utf-8

"""
Pour importer des modules venant d'autres dossiers:
export PYTHONPATH=$HOME/Bureau/Memoire/simulation/
"""

import numpy as np
import echange
import h5py


def evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit,loi, h5file, asyn_steps):

    individusAleatoires = np.arange(NbIndividus)

    res = []
    res.append(TableauFourmis.copy())
    m2 = []

    dset = h5file.create_dataset('q', shape=(1,TableauFourmis.shape[0]), dtype=TableauFourmis.dtype, maxshape=(None,TableauFourmis.shape[0]))
    dset[-1] = TableauFourmis

    for temps in range(NbSimul):
		
        echange.one_step(individusAleatoires, TableauFourmis, capaciteStock,loi, asyn_steps)

        res.append(TableauFourmis.copy())
        dset.resize(dset.shape[0]+1, axis=0)
        dset[-1] = TableauFourmis

        m2.append( np.sum(TableauFourmis**2) )

    return res, m2
