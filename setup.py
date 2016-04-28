# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "mparticle"
VERSION = "0.9.0"



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
    description="""`Package Documentation <https://github.com/mParticle/mparticle-python-sdk/wiki>`_.
    This SDK is a helper library for the mParticle server-to-server HTTP API, it exposes mParticle's schema as simple models and provides an HTTP client interface. This SDK is stateless and will only send the data that you populate, whereas our mobile SDKs will automatically collect app and device information, session events, install events, and maintain persistence.""",
    author_email="support@mparticle.com",
    url="http://www.mparticle.com",
    keywords=["mParticle"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
    'Development Status :: 4 - Beta', 
    'Environment :: Console', 
    'License :: OSI Approved :: Apache Software License', 
    'Programming Language :: Python', 
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)


