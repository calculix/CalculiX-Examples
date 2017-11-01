#!/usr/bin/python
import os

os.system("cgx -b pre.fbl")
os.system("ccx modal")
os.system("cgx -b shapes.fbl")
