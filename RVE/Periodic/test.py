#!/usr/bin/python
import os

os.system("cgx -b RVE.fbd")
os.system("periodic.py all.msh")
os.system("ccx Solve")
os.system("cgx -b post.fbd")
