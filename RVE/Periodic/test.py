#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b RVE.fbd")
os.system("periodic.py all.msh")
os.system("ccx Solve")
os.system("cgx -b post.fbd")
