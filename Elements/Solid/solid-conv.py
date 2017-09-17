#!/usr/bin/python
"""
This script runs a convergence study for solid elements
"""
#from subprocess import call
import os
import pylab
import numpy
import re

# Calculix solid element types with their cgx counterparts.
#~ eltyps={"C3D8":"he8",
    #~ "C3D4":"te4",
    #~ "C3D10":"te10"}
eltyps={"C3D8":"he8",
    "C3D8R":"he8r",
    "C3D8I":"he8i",
    "C3D20":"he20",
    "C3D20R":"he20r",
    "C3D4":"te4",
    "C3D10":"te10"}
#elsizes=[500,250,100,50,25,10,5]
elsizes=[100,50,25,10,5]
# read the template fbd file
f = open("solid.fbd","r")
lines=f.readlines()
f.close()
# loop over element types
for elty in eltyps.keys():
    # open results summary file
    fdata=open(elty+".txt","w")
    fdata.write("# size NoN smax umax\n")
    # loop over element sizes
    for elsize in elsizes:
        print elty, elsize
        # modify solid.fbd and write output to solid-auto.fbd
        fout = open("solid_auto.fbd", "w")
        for line in lines:
            # set element type
            if line.startswith("valu Etyp"):
                line="valu Etyp "+eltyps[elty]+"\n"
                # set element size
            if line.startswith("div all auto"):
                line="div all auto "+str(elsize)+"\n"
                if elty.startswith("C3D8") or elty.startswith("C3D4"):
                    # increase the node distance for linear elements
                    line=line+"div all div 2\n"
                    elsize=elsize*2
                fout.write("ulin "+elty+" "+str(elsize)+"\n")
            fout.write(line)
        fout.write("quit\n")
        fout.close()
        # run solid_auto.fbd (preprocessing, solving and postprocessing)
        os.system("cgx -b solid_auto.fbd")
        # get number of nodes from solid.frd
        f=open("solid.frd")
        for line in f:
            if line.startswith("    2C"):
                nnode=int(line.split()[1])
        f.close()
        print "Knotenzahl ", nnode
        # get smax from smax.txt
        smax=numpy.genfromtxt("smax.txt")[3]
        # get umax from umax.txt
        smin=numpy.genfromtxt("smin.txt")[3]
        # get umax from umax.txt
        umax=numpy.genfromtxt("umax.txt")[3]
        # rename the stress plot
        os.system("mv hcpy_1.png "+"solid_"+elty+"_"+str(elsize)+"_S.png")
        # write the values to the data file
        fdata.write(str(elsize)+" "+str(nnode)+" "+str((smax-smin)/2.)+" "+str(abs(umax))+"\n")
    fdata.close()
