#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b b32.fbd")
os.system("ccx u1General")
os.system("sed -n '4,14 p' u1General.dat > u1.txt")
os.system("gnuplot u1.plt")
