# encoding: utf-8
from setuptools import setup, find_packages

from minicms import __version__ as version

setup(
    name='minicms',
    version=version,
    author='Pavel Puchkin',
    author_email='neoascetic@gmail.com',
    url='https://github.com/neoascetic/minicms',

    description='Simple CMS app for Django which supports i18n',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
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
        'markdown >= 2.1',
    ),
)
