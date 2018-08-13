import setuptools

NAME = 'trainer'
VERSION = '1.0'
TENSORFLOW_TRANSFORM = 'tensorflow-transform==0.1.10'

if __name__ == '__main__':
    print(setuptools.find_packages())
    setuptools.setup(name=NAME, version=VERSION, packages=setuptools.find_packages(),
                     install_requires=[TENSORFLOW_TRANSFORM])
