#!/usr/bin/env python
"""execute all test scripts in the example collection"""
import os, fnmatch, multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Locate all files matching supplied filename pattern in and below
# current directory.
counter=1
for path, dirs, files in os.walk(os.path.abspath(os.curdir)):
    for filename in fnmatch.filter(files, "test.py"):
        test=os.path.join(path, filename)
        print(test)
        # change to the example directory
        os.chdir(path)
        # execute the test script
        os.system("./test.py > test.log")
