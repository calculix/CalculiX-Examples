#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
os.system("../../Scripts/param.py par.ct.geo a=21.0")
os.system("cgx -b ct.fbd")
os.system("../../Scripts/param.py par.ct.geo a=20.5")
os.system("cgx -b ct.fbd")
os.system("cgx -b path.fbd")
