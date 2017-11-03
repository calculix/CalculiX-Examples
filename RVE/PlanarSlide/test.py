#!/usr/bin/python
import os

os.system("cgx -b RVE.fbd")
os.system("ccx Zug")
os.system("monitor.py Zug")
os.system("cgx -b post.fbd")
