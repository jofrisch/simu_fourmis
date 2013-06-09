# cython: profile=False
import numpy as np
cimport numpy as np
cimport cython
from libc.stdlib cimport rand, RAND_MAX

@cython.cdivision(True)
cdef double PR_lin(int charge, int capa):
    return 1.-charge*1./capa

@cython.boundscheck(False)
@cython.wraparound(False)
def one_step(np.ndarray[np.int64_t, ndim=1] individusAleatoires, np.ndarray[np.int64_t, ndim=1] TableauFourmis, int capa):
    cdef int NbIndividus = TableauFourmis.shape[0]
    cdef int k, l, don
    cdef unsigned int i
    cdef double x,y, P1, P2
    PR=PR_lin

    cdef np.ndarray[np.float64_t, ndim=1] draws = np.random.random(NbIndividus)

    np.random.shuffle(individusAleatoires)

    for i in range(NbIndividus/2):
        k = individusAleatoires[2*i]
        l = individusAleatoires[2*i+1]
        
        ChargePremier = TableauFourmis[k]
        ChargeSecond = TableauFourmis[l]
        
        x = draws[2*i]
        y = draws[2*i+1]

        P1 = PR(ChargePremier, capa)
        P2 = PR(ChargeSecond, capa)

        if x<P1 and y>P2:
            don = 1
        elif x>P1 and y<P2:
            don = -1
        else:
            don=0
            
        TableauFourmis[k] = TableauFourmis[k]+don
        TableauFourmis[l] = TableauFourmis[l]-don

        return
