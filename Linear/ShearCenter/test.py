#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("param.py par.II-pre.fbl")
os.system("cgx -b II-pre.fbl")
os.system("ccx II")
os.system("cgx -b II-post.fbl")
