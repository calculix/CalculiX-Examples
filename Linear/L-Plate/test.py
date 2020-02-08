#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("../../Scripts/param.py par.run.fbl")
os.system("cgx -b run.fbl")
os.system("cgx -b vmodes.fbd")
os.system("cgx -b bmodes.fbd")
