from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='trezarpi-lcd',
    version='0.1.0',
    description='TrezarPI - LCD library',
    long_description=long_description,
    url='https://github.com/mkapusnik/trezarpi',
    author='Michal Kapusnik',
    author_email='michal.kapusnik@gmail.com',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha'
    ],

    keywords='tzc crypto raspberry',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['daemonize', 'gpio', 'python-bitcoinrpc', 'python-daemon']
)