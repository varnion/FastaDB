#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='FastaDB',
    version='0.0.1',
    description="Fasta File archiver for biological annotation and records",
    long_description=readme + '\n\n' + history,
    author="Vinicius Mesel",
    author_email='vinicius@bigsp.com.br',
    url='https://github.com/vmesel/fastadb',
    packages=[
        'FastaDB',
    ],
    package_dir={'FastaDB':
                 'FastaDB'},
    entry_points={
        'console_scripts': [
            'fastadb=fastadb.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='fastadb',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='test',
    tests_require=test_requirements
)
