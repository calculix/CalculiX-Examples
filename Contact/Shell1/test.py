#!/usr/bin/python
import os

os.system("cgx -b pre.fbd")
os.system("ccx tie")
os.system("monitor.py tie")
os.system("cgx -b post.fbd")









