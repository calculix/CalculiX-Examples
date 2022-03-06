#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy

de = numpy.genfromtxt("total internal energy_EDRAHT.txt")
dm = numpy.genfromtxt("forces fx,fy,fz_NROT.txt")
plt.plot(de[:,0],de[:,1],'b',dm[:,0],dm[:,3],'r')
plt.grid(True)
plt.xlim([0,1])
plt.xlabel("t")
plt.ylabel("y")
plt.legend(["Energy","Moment"],loc=0)
plt.savefig("Biegung-history")
