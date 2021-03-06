#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import exists
from setuptools import setup, find_packages

author = 'Mathcube'
email = 'mathcube7@gmail.com'
description = 'A more convenient API for pencil and paper calculations with sympy'
name = 'sympymod'
year = '2021'
url = ''
version = '0.0.3'

setup(
    name=name,
    author=author,
    author_email=email,
    url=url,
    version=version,
    packages=find_packages(),
    package_dir={name: name},
    include_package_data=True,
    license='MIT',
    description=description,
    long_description=open('README.md').read() if exists('README.md') else '',
    long_description_content_type="text/markdown",
    install_requires=['sphinx',
                      ],
    python_requires=">=3.6",
    classifiers=['Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 ],
    platforms=['ALL'],
)
