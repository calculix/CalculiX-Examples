#!/usr/bin/python
"""
This script plots the results of a convergence study for solid elements
"""
import os
import pylab
import numpy
# reference values, see
sref=0.0924102
wref=0.000170152
# List of the element types to process (text files)
eltyps=["C3D8",
	"C3D8R",
	"C3D8I",
	"C3D20",
	"C3D20R",
	"C3D4",
	"C3D10"]
pylab.figure(figsize=(10, 5.0), dpi=100)
pylab.subplot(1,2,1)
pylab.title("Stress")
# pylab.hold(True) # deprecated
for elty in eltyps:
    data = numpy.genfromtxt(elty+".txt")
    pylab.plot(data[:,1],data[:,2]/sref,"o-")
pylab.xscale("log")
pylab.xlabel('Number of nodes')
pylab.ylabel('Max $\sigma / \sigma_{\mathrm{ref}}$')
pylab.grid(True)
pylab.subplot(1,2,2)
pylab.title("Displacement")
# pylab.hold(True) # deprecated
for elty in eltyps:
    data = numpy.genfromtxt(elty+".txt")
    pylab.plot(data[:,1],data[:,3]/wref,"o-")
pylab.xscale("log")
pylab.xlabel('Number of nodes')
pylab.ylabel('Max $u / u_{\mathrm{ref}}$')
pylab.ylim([0,1.2])
pylab.grid(True)
pylab.legend(eltyps,loc="lower right")
pylab.tight_layout()
pylab.savefig("solid.svg",format="svg")
pylab.show()
