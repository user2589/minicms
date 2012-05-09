# encoding: utf-8

import os
from setuptools import setup


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='minicms',
    version='0.1.1',
    author='Pavel Puchkin',
    author_email='neoascetic@gmail.com',
    url='https://github.com/neoascetic/minicms',

    description='Simple CMS app for Django which supports i18n',
    long_description=read('README.rst'),
    packages=('minicms',),
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",

        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ),

    install_requires=(
        'django_markdown',
        'markdown >= 2.1'
    ),
)
