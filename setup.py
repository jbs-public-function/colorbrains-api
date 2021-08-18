#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup


NAME = 'colorbrains-api'
DESCRIPTION = 'colorbrains-api project for ML generated colorschemes'
URL = 'https://github.com/jbs-public-function/colorbrains-api'
EMAIL = 'jbs.public.function@gmail.com'
AUTHOR = 'James B'
REQUIRES_PYTHON = '>=3.7.9'
VERSION = '0.1.0'
LICENSE = 'BSD 3-Clause License'
DIR = os.path.dirname(__file__)


def read_file_as_txt(filename, alternate_txt=''):
    try:
        with io.open(os.path.join(os.path.abspath(DIR), filename), encoding='utf-8') as f:
            return '\n' + f.read()
    except FileNotFoundError:
        return alternate_txt


def read_requirements_file(requirements_filename):
    requirements = read_file_as_txt(requirements_filename).split('\n')
    return [requirement.strip() for requirement in requirements if '#' not in requirement and len(requirement.strip()) > 0]


def read_requirements():
    return read_requirements_file('requirements.txt')


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read_file_as_txt('README.md', DESCRIPTION),
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=['colorbrains'],
    install_requires=read_requirements(),
    include_package_data=True,
    license=read_file_as_txt('LICENSE', LICENSE),
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
