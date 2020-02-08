#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b RVE.fbd")
os.system("ccx Zug")
os.system("../../Scripts/monitor.py Zug")
os.system("cgx -b verify.fbd")
os.system("cgx -b post.fbd")
