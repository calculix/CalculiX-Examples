#!/usr/bin/python
import os
os.system("ccx u1general")
os.system("sed -n '4,14 p' u1general.dat > u1.txt")
os.system("gnuplot u1.plt")
