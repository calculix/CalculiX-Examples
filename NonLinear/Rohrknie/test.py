#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

os.system("cgx -b shell-modal.fbd")
os.system("cgx -b shell-sym-modal.fbd")
os.system("cgx -b solid-modal.fbd")
os.system("cgx -b solid.fbd")
os.system("ccx solid-static")
os.system("monitor.py solid-static")
os.system("cgx -b post-solid-static.fbd")
os.system("cgx -b solid-sym-modal.fbd")
