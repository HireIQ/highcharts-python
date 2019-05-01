#!/usr/bin/env python

from distutils.core import setup

setup(
    name='highcharts-python',
    version='0.4',
    description='Python interface for creating highcharts config objects.',
    packages=['highcharts', 'highcharts.lib'],
    install_requires=['six'],
)
