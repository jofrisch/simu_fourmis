# coding:utf-8

"""
Pour importer des modules venant d'autres dossiers:
export PYTHONPATH=$HOME/Bureau/Memoire/simulation/
"""

import numpy as np
import echange



def evolution(TableauFourmis,NbSimul,NbIndividus,capaciteStock,ChargeUnit,loi):

    individusAleatoires = np.arange(NbIndividus)

    res = []
    res.append(TableauFourmis.copy())

    for temps in range(NbSimul):
		
        echange.one_step(individusAleatoires, TableauFourmis, capaciteStock,loi)#, echange.PR_lin)

        res.append(TableauFourmis.copy())
    return res
