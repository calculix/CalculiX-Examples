#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("param.py par.run.fbl")
os.system("cgx -b run.fbl")
os.system("param.py par.run1.fbl")
os.system("cgx -b run1.fbl")
