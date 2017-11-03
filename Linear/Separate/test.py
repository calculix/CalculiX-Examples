#!/usr/bin/python
import os

os.system("cgx -b pre.fbd")
os.system("ccx nodal")
os.system("ccx element")
os.system("cgx -b post-n.fbd")
os.system("cgx -b post-e.fbd")
