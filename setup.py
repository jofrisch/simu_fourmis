from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy as np
import os

ran_base = os.path.join(os.path.dirname(np.__file__),'random')

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("echange", ["echange_mod.pyx"], extra_objects = [os.path.join(ran_base,'mtrand.so')])],
    include_dirs=[ran_base]
)
