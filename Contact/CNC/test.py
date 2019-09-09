#!/usr/bin/python
import os

os.system("cgx -b profile.fbd")
os.system("cgx -b winkel.fbd")
os.system("cgx -b rod.fbd")
os.system("cgx -b SK.fbd")
os.system("cgx -b assembly.fbd")
os.system("ccx solve")
os.system("cgx -b post.fbd")
