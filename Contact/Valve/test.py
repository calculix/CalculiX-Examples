#!/usr/bin/python
import os

os.system("param.py par.pre.fbd")
os.system("cgx -b pre.fbd")
os.system("ccx valve")
os.system("monitor.py valve")
os.system("cgx -b post.fbd")
