#!/usr/bin/python
import os

os.system("param.py par.run.fbl")
os.system("cgx -b run.fbl")
os.system("cgx -b vmodes.fbd")
os.system("cgx -b bmodes.fbd")
