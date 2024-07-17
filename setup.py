# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

# Function to read the requirements from requirements.txt
def read_requirements():
	with open('requirements.txt', 'r') as f:
		return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# get version from __version__ variable in pivot_table/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('pivot_table/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

# Use the read_requirements function to get the list of requirements
requirements = read_requirements()

setup(
	name='pivot_table',
	version=version,
	description='Pivot Tables using PivotTable.js',
	author='vijaywm',
	author_email='vijay_wm@yahoo.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=requirements,
	# Remove the dependency_links if not used or update accordingly
)
