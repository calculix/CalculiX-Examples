#!/usr/bin/python
"""
Test for the pillow example
"""
#from subprocess import call
import os
import pylab
import numpy
import re

# The example is run for four element types
eltyps={"S8":"qu8",
        "S8R":"qu8",
        "S4":"qu4",
        "S4R":"qu4"}
# read the template fbd file
f = open("pre.fbd","r")
lines=f.readlines()
f.close()
# loop over element types
for elty in eltyps.keys():
    # open results summary file
    print elty
    # read pre.fbd and write it to pre-auto.fbd
    fout = open("pre_auto.fbd", "w")
    fout.write("text "+elty+"\n")
    for line in lines:
        # set element type
        if line.startswith("valu Etyp"):
            line="valu Etyp "+eltyps[elty]+"\n"
        fout.write(line)
    fout.write("quit\n")
    fout.close()
    # run pre_auto.fbd (preprocessing, solving and postprocessing)
    os.system("cgx -b pre_auto.fbd")
    # set the correct ccx element type
    print("sed -i -e:1 -e's/TYPE=\([A-Z0-9]*\)/TYPE="+elty+"/' all.msh")
    os.system("sed -i -e:1 -e's/TYPE=\([A-Z0-9]*\)/TYPE="+elty+"/' all.msh")
    # run simulation and store the images.
    os.system("ccx static")
    os.system("../Scripts/monitor.py static")
    os.system("cgx -b post.fbd")
    os.system("mv expanded.png Refs/expanded-"+elty.lower()+".png")
    os.system("mv cuty0.png Refs/cuty0-"+elty.lower()+".png")
    os.system("mv static.png Refs/static-"+elty.lower()+".png")
