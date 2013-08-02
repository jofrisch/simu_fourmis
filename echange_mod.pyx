# cython: profile=False
import numpy as np
cimport numpy as np
cimport cython
from libc.stdlib cimport rand, RAND_MAX
from libc.stdlib cimport malloc, free

cdef extern from "randomkit.h":
    cdef enum rk_error:
        RK_NOERR
        RK_ENODEV
        RK_ERR_MAX

    ctypedef struct rk_state:
        unsigned long key[624]
        int pos
        int has_gauss
        double gauss
        int has_binomial
        double psave
        long nsave
        double r
        double q
        double fm
        long m
        double p1
        double xm
        double xl
        double xr
        double c
        double laml
        double lamr
        double p2
        double p3
        double p4

    # 0xFFFFFFFFUL
    cdef unsigned long RK_MAX
    cdef unsigned long rk_interval(unsigned long max, rk_state *state)
    cdef rk_error rk_randomseed(rk_state *state)

cdef rk_state *s = <rk_state *> malloc(sizeof(rk_state))
cdef local_error
local_error = rk_randomseed(s)

@cython.cdivision(True)
cdef double PR_lin(int charge, int capa):
    return 1.-charge*1./capa

@cython.cdivision(True)
cdef double PR_cste(int charge, int capa):
    if 0<charge<capa:
        return 0.5
    elif charge == 0:
        return 1
    elif charge == capa:
        return 0

@cython.cdivision(True)
cdef double PR_anti(int charge, int capa):
    if 0<charge<capa:
        return charge*1./capa
    elif charge == 0:
        return 1
    elif charge == capa:
        return 0

@cython.cdivision(True)
cdef double PR_vague(int charge, int capa):
    cdef double l
    l = charge*1./capa
    if 0<charge<capa:
        return -2*l**2+1.5*l+0.5
    elif charge == 0:
        return 1
    elif charge == capa:
        return 0



@cython.boundscheck(False)
@cython.wraparound(False)
cdef void cshuffle(np.ndarray[np.int64_t, ndim=1] x):
    cdef int i
    i = x.shape[0]-1
    while i > 0:
        j = rk_interval(i, s)
        x[i], x[j] = x[j], x[i]
        i = i - 1

@cython.boundscheck(False)
@cython.wraparound(False)
def one_step(np.ndarray[np.int64_t, ndim=1] individusAleatoires, np.ndarray[np.int64_t, ndim=1] TableauFourmis, int capa, int loi, int asyn_steps):
    cdef int NbIndividus = TableauFourmis.shape[0]
    cdef int k, l, don
    cdef unsigned int i
    cdef int ChargePremier, ChargeSecond
    cdef int n_steps
    cdef double x,y, P1, P2

    if loi == 0:
        PR=PR_cste
    elif loi == 1:
        PR = PR_lin
    elif loi == 2:
        PR = PR_anti
    elif loi == 3:
        PR = PR_vague
    else:
        print "ERREUR, MAUVAIS ARGUMENT DEFINISSANT LA LOI D'ECHANGE"
        return

    cdef np.ndarray[np.float64_t, ndim=1] draws = np.random.random(NbIndividus)

    if asyn_steps<0:
        cshuffle(individusAleatoires)
        n_steps = NbIndividus/2
    else:
        n_steps = asyn_steps
    
    for i in range(n_steps):
        if asyn_steps<0:
            k = individusAleatoires[2*i]
            l = individusAleatoires[2*i+1]
        else:
            cshuffle(individusAleatoires)
            k = individusAleatoires[0]
            l = individusAleatoires[1]

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

def distribute(np.ndarray[np.int64_t, ndim=1] TableauFourmis, int c_moyenne, int capa):
    cdef int i, j
    cdef int l = TableauFourmis.shape[0]-1
    for i in range(c_moyenne*(l+1)):
        while True:
            j = rk_interval(l, s)
            if TableauFourmis[j]<capa:
                TableauFourmis[j] += 1
                break
    return
