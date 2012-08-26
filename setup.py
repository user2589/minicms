# encoding: utf-8
from setuptools import setup, find_packages

from minicms import VERSION, LICENSE, PROJECT

setup(
    name=PROJECT,
    version=VERSION,
    description='Simple CMS app for Django which supports i18n',
    long_description=open('README.rst').read(),
    license=LICENSE,

    author='Pavel Puchkin',
    author_email='neoascetic@gmail.com',
    url='https://github.com/neoascetic/minicms',

    keywords='django cms',
    classifiers=(
        "Programming Language :: Python",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",

        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
    ),

    packages=find_packages(),
    include_package_data=True,
    dependency_links = (
        'https://github.com/user2589/django-sortable/tarball/master#egg=django-sortable-0.2.0',
        'https://github.com/neoascetic/django-pagedown/tarball/master#egg=django-pagedown-0.0.2',
    ),
    install_requires = (
        'django >= 1.3',
        'django-sortable >= 0.2.0',
        'django-pagedown >= 0.0.2',

        'markdown >= 2.1',
    ),
)
