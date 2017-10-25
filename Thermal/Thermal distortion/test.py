#!/usr/bin/python
import os

for contact in ('tie', 'pc-ss'):
    os.system("param.py par.pre.fbd contact=\"'"+contact+"'\"")
    os.system("cgx -b pre.fbd")
    os.system("ccx Tjoint")
    os.system("cgx -b post.fbd")





