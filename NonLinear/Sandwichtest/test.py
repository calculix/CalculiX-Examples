#!/usr/bin/python
import os

os.system("cgx -b pre.fbl")
os.system("ccx Biegung")
os.system("monitor.py Biegung")
os.system("cgx -b post.fbl")









