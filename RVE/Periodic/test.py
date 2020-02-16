#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
os.system("cgx -b RVE.fbd")
os.system("../../Scripts/periodic.py all.msh")
os.system("ccx Solve")
os.system("cgx -b post.fbd")
