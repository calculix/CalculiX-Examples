#!/usr/bin/python
import os
os.system("ccx u1General")
os.system("sed -n '4,14 p' u1General.dat > u1.txt")
os.system("gnuplot u1.plt")
