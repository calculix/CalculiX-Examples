#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
os.system("cgx -b pre.fbl")
os.system("ccx solve")
os.system("cgx -b shapes.fbd")
os.system("ccx trans")
os.system("../../Scripts/monitor.py trans")
os.system("cgx -b post.fbl")
os.system("ccx trfix")
os.system("cgx -b trfix.fbl")
