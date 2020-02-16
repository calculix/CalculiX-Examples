#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
os.system("cgx -b shell-modal.fbd")
os.system("cgx -b shell-sym-modal.fbd")
os.system("cgx -b solid-modal.fbd")
os.system("cgx -b solid.fbd")
os.system("ccx solid-static")
os.system("../../Scripts/monitor.py solid-static")
os.system("cgx -b post-solid-static.fbd")
os.system("cgx -b solid-sym-modal.fbd")
