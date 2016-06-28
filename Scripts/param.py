#!/usr/bin/python
"""
This script searches for strings in
angle brackets <...>
If the string is an assignment (e.g. "a=1"), it is executed.
If the string is an expression (e.g. "a+a"), it is
evaluated and the result is placed instead of the <...> construct.
"""
import sys
import re
import glob

# processing command line arguments, get the
# jobname
if len(sys.argv)==1:
    print "No filename given."
    files=glob.glob("par.*")
    if len(files)==1:
        print "Found", files[0]
        source=files[0]
    else:
        print "Available par.* files:"
        for f in files:
            print "  ", f
        quit()
if len(sys.argv)>1:
    print "Using file:",sys.argv[1]
    source = sys.argv[1]

print("Source "+source)
if source.endswith(".par"):
    target = source[0:-4]
elif source.startswith("par."):
    target = source[4:]
print("Target "+target)
f = open(source,"r")
fo = open(target,"w")
# context dictionaries for evaluation
g={}
l={}
exec("from math import *",g,l)
for line in f:
    # split line into dead and active strings
    s=re.split(r"<([^>]*)>",line)
    # build the output string
    outline=""
    # iterate over pairs of dead and active strings
    for i in range(0,len(s),2):
        outline=outline+s[i]
        if not i+1==len(s):
            # if an active string is available
            active=s[i+1]
            if active.find("=")!=-1:
                # active string contains assignment
                exec(active,g,l)
                res=active
                print(active)
            else:
                # active string is an expression
                res=str(eval(active,g,l))
            outline=outline+res
    fo.write(outline)
fo.close()
f.close()
