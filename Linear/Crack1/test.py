#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("param.py par.ct.geo a=21.0")
os.system("cgx -b ct.fbd")
os.system("param.py par.ct.geo a=20.5")
os.system("cgx -b ct.fbd")
os.system("cgx -b path.fbd")
