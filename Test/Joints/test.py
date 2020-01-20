#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("param.py par.pre.fbl")
os.system("cgx -b pre.fbl")
os.system("cgx -b dist.fbl")
os.system("cgx -b kin.fbl")
os.system("param.py par.pre2.fbl")
os.system("cgx -b pre2.fbl")
os.system("cgx -b kin2.fbl")
