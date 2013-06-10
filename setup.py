from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("echange", ["echange_mod.pyx"], extra_objects = ['/usr/lib/pymodules/python2.7/numpy/random/mtrand.so'])],
    include_dirs=['/usr/lib/pymodules/python2.7/numpy/random/']
)
