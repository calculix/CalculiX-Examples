#!/usr/bin/python
import os
import glob
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# preprocessing
if 1:
    toRemovePre = (
        "*.nam",
        "*.bou",
        "*.sur",
        "hcpy*.png",
        "symy.png",
        "wfix.png",
        "parts.png",
        "contact.png",
        "all.msh",
        "rb1.inp")

    print "removing files"
    for spec in toRemovePre:
        files=glob.glob(spec)
        for f in files:
            print f
            os.remove(f)
    os.system("cgx -b pre.fbd")

# solve, can take a while
if 1:
    os.remove("Biegung.frd")
    os.remove("Biegung.dat")
    os.remove("Biegung.sta")
    os.remove("Biegung.cvg")
    os.system("ccx Biegung >>Biegung.log")

# convergence plot, reaction-time-plot
if 1:
    try:
        os.remove("Biegung.png")
    except:
        0
    os.remove("Biegung-history.png")
    files=glob.glob("force*.txt")
    for f in files:
        os.remove(f)
    files=glob.glob("total*.txt")
    for f in files:
            os.remove(f)
    os.remove("movie.gif")
    os.remove("deform.png")
    os.remove("PE.png")

    os.system("../../Scripts/monitor.py Biegung")
    os.system("../../Scripts/dat2txt.py Biegung")
    os.system("./Biegung.py")
    os.system("cgx -b Animation.fbd")
    os.system("cgx -b post.fbd")
