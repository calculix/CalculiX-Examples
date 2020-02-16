#!/usr/bin/python
"""
Test for the pillow example
"""
#from subprocess import call
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# The example is run for four element types
eltyps={"S8":"qu8",
        "S8R":"qu8r",
        "S4":"qu4",
        "S4R":"qu4r"}
# read the template fbd file
f = open("run.fbd","r")
lines=f.readlines()
f.close()
# loop over element types
for elty in eltyps.keys():
    # open results summary file
    print elty
    # read pre.fbd and write it to pre-auto.fbd
    fout = open("run_auto.fbd", "w")
    fout.write("ulin "+elty+"\n")
    for line in lines:
        # set element type
        if line.startswith("valu Etyp"):
            line="valu Etyp "+eltyps[elty]+"\n"
        fout.write(line)
    fout.write("quit\n")
    fout.close()
    # run run_auto.fbd (preprocessing, solving and postprocessing)
    os.system("cgx -b run_auto.fbd")
    # store the images.
    os.system("../Scripts/monitor.py static")
    os.system("mv expanded.png Refs/expanded-"+elty.lower()+".png")
    os.system("mv cuty0.png Refs/cuty0-"+elty.lower()+".png")
    os.system("mv static.png Refs/static-"+elty.lower()+".png")
