#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b pre.fbl")
os.system("ccx solve")
os.system("../../Scripts/monitor.py solve")
os.system("cgx -b anim.fbl")
os.system("cgx -b post.fbl")
