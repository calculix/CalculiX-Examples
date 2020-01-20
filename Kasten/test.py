#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b pre.fbd")
os.system("ccx Kasten")
os.system("monitor.py Kasten")
os.system("cgx -b post.fbd")
