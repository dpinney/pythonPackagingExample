#!/usr/bin/env python

from setuptools import setup

setup(
	name='addmult',
	version='1.3',
	description='An example of packaging. Feature: adds or multiplies numbers.',
	long_description_content_type='text/markdown',
	long_description=open('README.md').read(),
	author='David Pinney',
	author_email='david@pinney.org',
	url='https://github.com/dpinney/pythonPackagingExample/',
	packages=['addmult'],
	include_package_data=True,
	install_requires=['numpy'],
)