#!/usr/bin/env python
'''
Created on 07/12/2011

@author: Moises P. Sena "<moisespsena" + "@" + "gmail.com>"
'''

from distutils.cmd import Command
from setuptools import setup
from unittest.runner import TextTestRunner
from unittest.suite import TestSuite
import os
import re
import sys
import unittest
import shutil

THIS_PATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
PKG_DIR = os.path.join(THIS_PATH, "sdag")
TEST_DIR = os.path.join(THIS_PATH, "tests")

def read(fname):
    global THIS_PATH
    return open(os.path.join(THIS_PATH, fname)).read()

class TestCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self._dir = os.getcwd()

    def finalize_options(self):
        pass

    def run(self):
        global THIS_PATH, PKG_DIR, TEST_DIR
        
        sys.path.insert(0, PKG_DIR)
        
        suite = TestSuite()
        loaded = unittest.defaultTestLoader.discover(TEST_DIR, pattern='*Test.py')
        
        for all_test_suite in loaded:
            for test_suite in all_test_suite:
                suite.addTests(test_suite)
        
        runner = TextTestRunner(verbosity = 2)
        runner.run(suite)
          
class CleanCommand(Command):
    user_options = [ ]

    def initialize_options(self):
        self.rmPaths = [ ]
        
        for f in os.listdir(THIS_PATH):
            if re.search("(^(build|dist)$|\.egg-info)", f):
                self.rmPaths.append(f)
            
        for root, dirs, files in os.walk(THIS_PATH):
            for f in files:
                if f.endswith(".pyc") or f.endswith(".pyc"):
                    self.rmPaths.append(os.path.join(root, f))

    def finalize_options(self):
        pass
    
    def run(self):
        for p in self.rmPaths:
            if os.path.isdir(p):
                print("Remove directory: " + p)
                shutil.rmtree(p)
            else:
                print("Remove file     : " + p)
                os.unlink(p)
            
setup(
    name = "py-sdag",
    version = "1.0",
    author = "Moises P. Sena",
    author_email = "moisespsena@gmail.com",
    description = ("Simple Directed Acyclic Graph whith Cicle Detector and TopoloGical sorter utilities."),
    license = "BSD",
    keywords = "utils utilities directed graph digraph topological sorter simple",
    url = "https://github.com/moisespsena/py-sdag",
    packages=["sdag"],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7" 
    ],
    cmdclass={'test' : TestCommand, 'clean': CleanCommand}
)
