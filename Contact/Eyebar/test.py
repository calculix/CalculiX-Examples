#!/usr/bin/python
import os

os.system("param.py par.eyebar.fbd")
os.system("cgx -b eyebar.fbd")
os.system("ccx eyebar")
os.system("monitor.py eyebar")
os.system("cgx -b post.fbd")
