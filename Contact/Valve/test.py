#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("../../Scripts/param.py par.pre.fbd")
os.system("cgx -b pre.fbd")
os.system("ccx valve")
os.system("../../Scripts/monitor.py valve")
os.system("cgx -b post.fbd")
