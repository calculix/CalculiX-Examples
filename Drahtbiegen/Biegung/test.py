#!/usr/bin/python

import os
import glob
import multiprocessing
import shutil


# Provide access to the helper scripts
def modify_path():
    scripts_dir = os.path.dirname(__file__)
    while not 'Scripts' in os.listdir(scripts_dir):
        scripts_dir = os.path.abspath(os.path.join(scripts_dir, '..'))
    scripts_dir = os.path.join(scripts_dir, 'Scripts')
    if not scripts_dir in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + scripts_dir
    print '\nPATH = {}\n'.format(os.environ['PATH'])


# preprocessing
def pre():
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
def solve():
    try: os.remove("Biegung.frd")
    except: pass
    try: os.remove("Biegung.dat")
    except: pass
    try: os.remove("Biegung.sta")
    except: pass
    try: os.remove("Biegung.cvg")
    except: pass
    os.system("ccx Biegung >>Biegung.log")


# convergence plot, reaction-time-plot
def post():
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

    os.system("monitor.py Biegung")
    os.system("dat2txt.py Biegung")
    os.system("./Biegung.py")
    os.system("cgx -b Animation.fbd")
    os.system("cgx -b post.fbd")


# Move new files and folders to 'Refs'
def move(old_snap):
    new_snap = os.listdir(os.curdir)
    if not os.path.exists('Refs'):
        os.mkdir('Refs')
    for f in new_snap:
        if not f in old_snap:
            fname = os.path.basename(f)
            new_name = os.path.join(os.curdir, 'Refs', fname)
            if os.path.isfile(new_name):
                os.remove(new_name)
            if os.path.isdir(new_name):
                shutil.rmtree(new_name)
            os.rename(f, new_name)


if __name__ == '__main__':

    # Enable multithreading for ccx
    os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

    # Explicitly move to example's directory
    os.chdir(os.path.dirname(__file__))

    # Run the example
    modify_path()
    snap = os.listdir(os.curdir)
    pre()
    solve()
    post()
    move(snap)
