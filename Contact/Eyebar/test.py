#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("param.py par.eyebar.fbd")
os.system("cgx -b eyebar.fbd")
os.system("ccx eyebar")
os.system("monitor.py eyebar")
os.system("cgx -b post.fbd")
