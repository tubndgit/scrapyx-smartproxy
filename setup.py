#!/usr/bin/env python
import sys
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='scrapyx-smartproxy',
        version='0.1.1',        
        description='SmartProxy middleware for Scrapy',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Henry B.',
        author_email='tubnd.younet@gmail.com',
        url='https://github.com/tubndgit/scrapyx-smartproxy',
        download_url = 'https://github.com/tubndgit/scrapyx-smartproxy/archive/master.zip', 
        packages=['scrapyx_smartproxy'],
        install_requires = [],
        license='MIT',
        python_requires='>=2.7',
    )