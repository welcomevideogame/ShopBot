from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("items", ["items.pyx"]),
    Extension("utilities", ["utilities.pyx"]),
]

setup(
    name="Cythonized StoreItems and Utilities",
    ext_modules=cythonize(extensions),
)