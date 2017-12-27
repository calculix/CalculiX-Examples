#!/usr/bin/python
"""execute all test scripts in the example collection"""
import os, fnmatch

# Locate all files matching supplied filename pattern in and below
# current directory.
counter=1
for path, dirs, files in os.walk(os.path.abspath(os.curdir)):
    for filename in fnmatch.filter(files, "test.py"):
        test=os.path.join(path, filename)
        print test
        # change to the example directory
        os.chdir(path)
        # execute the test script
        os.system("./test.py > test.log")
        
        
        
