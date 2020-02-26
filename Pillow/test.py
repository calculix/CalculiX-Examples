#!/usr/bin/python

""" Test for the pillow example """

import os
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


def run():
    # The example is run for four element types
    eltyps={"S8":"qu8",
            "S8R":"qu8r",
            "S4":"qu4",
            "S4R":"qu4r"}
    # read the template fbd file
    f = open("run.fbd","r")
    lines=f.readlines()
    f.close()
    # loop over element types
    for elty in eltyps.keys():
        # open results summary file
        print elty
        # read pre.fbd and write it to pre-auto.fbd
        fout = open("run_auto.fbd", "w")
        fout.write("ulin "+elty+"\n")
        for line in lines:
            # set element type
            if line.startswith("valu Etyp"):
                line="valu Etyp "+eltyps[elty]+"\n"
            fout.write(line)
        fout.write("quit\n")
        fout.close()
        # run run_auto.fbd (preprocessing, solving and postprocessing)
        os.system("cgx -b run_auto.fbd")
        # store the images.
        os.system("monitor.py static")
        os.system("mv expanded.png Refs/expanded-"+elty.lower()+".png")
        os.system("mv cuty0.png Refs/cuty0-"+elty.lower()+".png")
        os.system("mv static.png Refs/static-"+elty.lower()+".png")


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
    run()
    move(snap)
