import sys
import os
from distutils.core import setup

setup(
    name='csv2mysql', 
    version='0.1',
    packages=['csv2mysql'],
    package_dir={'csv2mysql' : '.'}, # look for package contents in current directory
    author='Richard Penman',
    description='Automatically parses a CSV file, creates MySQL table with appropriate field types, and then writes CSV data to the table',
    url='https://bitbucket.org/richardpenman/csv2mysql/',
    install_requires=['MySQLdb'],
    license='lgpl'
)
