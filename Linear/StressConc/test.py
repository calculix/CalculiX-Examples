#!/usr/bin/python
import os

os.system("param.py par.pre.fbl")
os.system("cgx -b pre.fbl")
os.system("ccx Stress")
os.system("cgx -b post.fbl")









