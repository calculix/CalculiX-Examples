#!/usr/bin/python
import os

os.system("cgx -b pre.fbl")
os.system("ccx Naht")
os.system("cgx -b post.fbl")
os.system("cgx -b plots.fbl")








