#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b pre.fbl")
os.system("ccx Naht")
os.system("cgx -b post.fbl")
os.system("cgx -b plots.fbl")
