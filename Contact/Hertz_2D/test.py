#!/usr/bin/python
import os

os.system("cgx -b pre.fbd")
os.system("ccx Hertz")
os.system("monitor.py Hertz")
os.system("cgx -b post.fbd")
os.system("cgx -b plots.fbd")
