#!/usr/bin/env python
import sys
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='scrapyx-smartproxy',
        version='0.1.1',        
        description='SmartProxy middleware for Scrapy',
        author='Henry B.',
        author_email='tubnd.younet@gmail.com',
        url='https://github.com/tubndgit/scrapyx-smartproxy',
        download_url = 'https://github.com/tubndgit/scrapyx-smartproxy/archive/master.zip', 
        packages=['scrapyx_smartproxy'],
        install_requires = [],
        license='MIT',
        python_requires='>=2.7',
    )