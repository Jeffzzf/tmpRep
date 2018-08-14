import os
import subprocess

import setuptools

NAME = 'trainer'
VERSION = '1.0'
TENSORFLOW_TRANSFORM = ['tensorflow-transform==0.1.10', 'scipy==1.1.0', 'Pillow==5.2.0', 'google-cloud-storage']

if __name__ == '__main__':
    setuptools.setup(name=NAME, version=VERSION, packages=setuptools.find_packages(),
                     install_requires=[TENSORFLOW_TRANSFORM])
