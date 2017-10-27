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

argParamsDict={}

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
    # check if parameter values are given on the command line
    if len(sys.argv)>2:
        argParams=sys.argv[2:]
        #print sys.argParams
        for argParam in argParams:
            key,val=argParam.split("=")
            print key,val
            argParamsDict[key]=val
        print argParamsDict    
            
# open files
print("Source: "+source)
if source.endswith(".par"):
    target = source[0:-4]
elif source.startswith("par."):
    target = source[4:]
print("Target: "+target)
f = open(source,"r")
fo = open(target,"w")
# context dictionaries for evaluation
# restriction to safe functions based on
# http://lybniz2.sourceforge.net/safeeval.html
from math import *
safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh']
#use the list to filter the local namespace
safe_dict = dict([ (k, locals().get(k, None)) for k in safe_list ])
#add any needed builtins back in.
safe_dict['abs'] = abs
safe_dict['int'] = int
l=safe_dict
g={"__builtins__":None}
ln=1 # linenumber for error message
#exec("from math import *",g,l)
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
                try:
                    exec(active,g,l)
                    res=active
                    val=str(eval(active[:active.find("=")],g,l))
                    print(active+"  ("+val+")")
                    # check for override by command line
                    key=active.split("=")[0]
                    if key in argParamsDict:
                        exec(key+"="+argParamsDict[key],g,l)
                        print "  Override by command line: ("+argParamsDict[key]+")"
                        res=key+"="+argParamsDict[key]
                except Exception as ex:
                    #template = "An exception of type {0} occured. Arguments:\n{1!r}"
                    #print template.format(type(ex).__name__, ex.args)
                    print "******* ERROR ********"
                    print "Line "+str(ln)+" in "+source+"\n"
                    print line
                    print ex.args[0]
                    if type(ex).__name__=="NameError":
                        print "Hint: Use <name=value> to define names."
                    exit()
            else:
                # active string is an expression
                try:
                    res=str(eval(active,g,l))
                except Exception as ex:
                    #template = "An exception of type {0} occured. Arguments:\n{1!r}"
                    #print template.format(type(ex).__name__, ex.args)
                    print "******* ERROR ********"
                    print "Line "+str(ln)+" in "+source+"\n"
                    print line
                    print ex.args[0]
                    if type(ex).__name__=="NameError":
                        print "Hint: Use <name=value> to define names."
                    exit()
            outline=outline+res
    fo.write(outline)
    ln=ln+1
fo.close()
f.close()
