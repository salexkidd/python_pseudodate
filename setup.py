# -*- coding:utf-8 -*-
from setuptools import setup
from setuptools import find_packages

from pseudodate import __version__
from pseudodate import __license__
from pseudodate import __author__
import pseudodate
import sys

sys.path.append('./pseudodate')
sys.path.append('./tests')


setup(
    name="python-pseudodate",
    author=__author__,
    author_email="salexkidd@gmail.com",
    version=__version__,
    packages=find_packages(),
    description="This module provide a specific pseudo datetime.",
    long_description=pseudodate.__doc__,
    url="https://github.com/salexkidd/python_pseudodate",
    keywords='pseudo datetime debug',
    license=__license__,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Utilities",
        ],
    test_suite="t.PseudoDateSuite",
    )
