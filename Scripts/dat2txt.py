#!/usr/bin/python
"""
This script extracts data from ccx dat-files
"""
import sys
import pylab
import re
import glob

data={}
pH = re.compile(' (.+) for set\\s(\\S+) and time  (.+)')
skip = 0 # if empty lines are to be skipped
body = 0 # if data lines are expected

# processing command line arguments, get the
# jobname
if len(sys.argv)==1:
    print "No jobname given."
    files=glob.glob("*.dat")
    if len(files)==1:
        print "Found", files[0]
        job=files[0]
    else:
        print "Available data files:"
        for f in files:
            print "  ", f
        quit()
if len(sys.argv)>1:
    print "Jobname:",sys.argv[1]
    job = sys.argv[1]+".dat"

f = open(job,"r")

for line in f:
    if skip: # if the line is known to be useless
	    skip = 0
	    continue
    line = line.replace("(","")
    line = line.replace(")","")
    line = line.replace("\n","")
    b = pH.match(line)
    if b: # a result header was found
        resname = b.group(1)
        group = b.group(2)
        res = resname+"_"+group
        time = float(b.group(3))
        if not (res in data.keys()): # new result type
            print res
            data[res] = open(res+".txt","w")
        data[res].write("\n"+str(time)+" ")
        skip = 1
        body = 1
    else:
        if len(line.split())==0:
            body = 0
            #data[resname].write("\n")
        elif body:
            data[res].write(line+" ")

for name in data.keys():
    data[name].close()
