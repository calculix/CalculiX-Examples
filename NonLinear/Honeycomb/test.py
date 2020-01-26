#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("param.py par.pre.fbl")
os.system("cgx -b pre.fbl")
os.system("ccx Biegung")
os.system("monitor.py Biegung")
os.system("cgx -b post.fbd")
