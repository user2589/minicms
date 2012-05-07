# encoding: utf-8

from setuptools import setup

setup(
    name='minicms',
    version='0.0.1',
    description='Simple CMS app for Django which supports i18n',

    author='Pavel Puchkin',
    author_email='neoascetic@gmail.com',

    packages=('minicms',),
    install_requires=('django_markdown',),
)
