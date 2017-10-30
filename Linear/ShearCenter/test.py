#!/usr/bin/python
import os

os.system("param.py par.II-pre.fbl")
os.system("cgx -b II-pre.fbl")
os.system("ccx II")
os.system("cgx -b II-post.fbl")








