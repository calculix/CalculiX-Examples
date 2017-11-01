#!/usr/bin/python
import os

os.system("cgx -b pre.fbl")
os.system("ccx solve")
os.system("monitor.py solve")
os.system("cgx -b anim.fbl")
os.system("cgx -b post.fbl")
