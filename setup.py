#! /usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Mikolaj Buchwald, mikolaj.buchwald@gmail.com'


from setuptools import setup, find_packages


setup(
    name="EEgSR",
    version="0.0.1",
    description="EEG/GSR acquisition and analysis tools.",
    license="BSD",
    keywords="EEG GSR BCI filtering plotting online realtime",
    url="http://mikbuch.github.io/eegsr",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
    install_requires=['scipy', 'matplotlib', 'sklearn'],
)
