# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "mparticle"
VERSION = "0.10.3"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description='Python client for the mParticle platform',
    long_description='`Package Documentation <https://github.com/mParticle/mparticle-python-sdk/wiki>`_ \n\nThis SDK is a helper library for the mParticle server-to-server HTTP API, it exposes mParticle\'s schema as simple models and provides an HTTP client interface. This SDK is stateless and will only send the data that you populate, whereas our mobile SDKs will automatically collect app and device information, session events, install events, and maintain persistence.',
    author='Sam Dozor',
    author_email="support@mparticle.com",
    url="https://github.com/mParticle/mparticle-python-sdk",
    keywords=["mparticle analytics marketing"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
