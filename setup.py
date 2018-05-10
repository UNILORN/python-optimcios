# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python_optimcios',
    version='0.0.2',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Yusuke Aoki',
    author_email='yuoyun6427.yuniron.komoron@gmail.com',
    install_requires=['numpy', 'websocket-client'],
    url='https://github.com/UNILORN/python-optimcios',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
