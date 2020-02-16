#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b b.fbd")
os.system("cgx -b sh.fbd")
os.system("cgx -b sm.fbd")
os.system("cgx -b sr.fbd")
os.system("cgx -b scd.fbd")
os.system("cgx -b sck.fbd")
