#!/usr/bin/python
import os

os.system("cgx -b pre.fbl")
os.system("ccx solve")
os.system("cgx -b shapes.fbd")
os.system("ccx trans")
os.system("monitor.py trans")
os.system("cgx -b post.fbl")
