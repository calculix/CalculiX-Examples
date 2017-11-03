#!/usr/bin/python
import os

os.system("param.py par.pre.fbl")
os.system("cgx -b pre.fbl")
os.system("ccx Biegung")
os.system("monitor.py Biegung")
os.system("cgx -b movie.fbl")
os.system("cgx -b chart.fbl")
