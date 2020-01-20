#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b run.fbd")
os.system("cgx -b runVT.fbd")
os.system("cgx -b run1.fbd")
os.system("cgx -b run2.fbd")
os.system("cgx -b VTdemo.fbd")
