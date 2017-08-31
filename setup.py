#!/usr/bin/env python

from distutils.core import setup
from setuptools.command.install import install

class PostInstallCommand(install):
	def run(self):
		print '!!!RUNNING DURING INSTALL PROCESS!!!'
		with open('~/DELETEME.txt','w+') as fileDrop:
			fileDrop.write('written during install of addmult python package as a test')
		install.run(self)

setup(
	name='addmult',
	version='1.3',
	description='An example of packaging. Feature: adds or multiplies numbers.',
	author='David Pinney',
	author_email='david@pinney.org',
	url='https://github.com/dpinney/pythonPackagingExample/',
	packages=['addmult'],
	# include all files in addmult directory including binaries:
	package_data={'addmult': ['*']},
	# run post-install commands:
	cmdclass={
		'install': PostInstallCommand,
	},
)