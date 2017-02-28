#!/usr/bin/env python

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = os.path.dirname(__file__)
exec(open(os.path.join(HERE, "construct25", "version.py")).read())

setup(
    name = "construct25",
    version = version_string, #@UndefinedVariable
    packages = [
        'construct25',
        'construct25.lib', 
        'construct25.formats', 
        'construct25.formats.data', 
        'construct25.formats.executable', 
        'construct25.formats.filesystem', 
        'construct25.formats.graphics',
        'construct25.protocols', 
        'construct25.protocols.application', 
        'construct25.protocols.layer2', 
        'construct25.protocols.layer3', 
        'construct25.protocols.layer4',
    ],
    license = "MIT",
    description = "A powerful declarative parser/builder for binary data",
    long_description = open(os.path.join(HERE, "README.rst")).read(),
    platforms = ["POSIX", "Windows"],
    url = "http://construct.readthedocs.org",
    author = "Arkadiusz Bulski, Tomer Filiba, Corbin Simpson",
    author_email = "arek.bulski@gmail.com, tomerfiliba@gmail.com, MostAwesomeDude@gmail.com",
    install_requires = [],
    requires = [],
    provides = ["construct25"],
    keywords = "construct, declarative, data structure, binary, parser, builder, pack, unpack",
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
    ],
)
