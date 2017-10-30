#!/usr/bin/python
import os

os.system("param.py par.ct.geo a=21.0")
os.system("cgx -b ct.fbd")
os.system("param.py par.ct.geo a=20.5")
os.system("cgx -b ct.fbd")
os.system("cgx -b path.fbd")








