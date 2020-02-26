#!/usr/bin/python

import os
import numpy
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


def run():
    etypes = ("qu4", "qu8", "qu8r")
    ctypes = ("tie", "equ", "pc-ns", "pc-ss")
    r=open("Results.md",'w')
    r.write("Elem   | Contact |        1 |        2 |        3 |        4 |        5 |        6 |        7 |        8 |        9 |       10\n")
    r.write(":--    | :--     | --:      | --:      | --:      | --:      | --:      | --:      | --:      | --:      | --:      | --:\n")
    for ctyp in ctypes:
        for etyp in etypes:
            # cleanup and create sim dir
            simPath = etyp + "_" + ctyp
            if os.path.exists(simPath):
                shutil.rmtree(simPath)
            os.mkdir(simPath)
            
            # get the command files
            shutil.copyfile("run.fbd",os.path.join(simPath,"run.fbd"))
            shutil.copyfile(ctyp+".inp",os.path.join(simPath,ctyp+".inp"))
            
            # generate parameter file
            with open(os.path.join(simPath, "values.fbd"), "w") as f:
                f.write("valu etyp " + etyp + "\n")
                f.write("valu ctyp " + ctyp + "\n")
                f.write("valu last quit \n")
            
            # run the simulation
            os.chdir(simPath)
            os.system("cgx -bg run.fbd")
            # extract frequencies
            os.system("dat2txt.py " + ctyp)
            freq=numpy.genfromtxt("Eigenvalues_1.txt",skip_header=1)
            os.chdir("..")
            
            # write frequencies to results file
            r.write("{0:6} | {1:6} ".format(etyp,ctyp))
            for i in range(10):
                # the frequency is the third last column (freq can have 4 or 5 columns)
                fcol=len(freq[0])-2
                r.write(" | " + "{0:8.3g}".format(freq[i,fcol]))
            r.write("\n")
    r.close()


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
