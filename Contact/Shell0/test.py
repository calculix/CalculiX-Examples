#!/usr/bin/python
import os
import glob
import shutil
import numpy
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

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
        f = open(os.path.join(simPath,"values.fbd"),'w')
        f.write("valu etyp " + etyp + "\n")
        f.write("valu ctyp " + ctyp + "\n")
        f.write("valu last quit \n")
        
        
        f.close()
        
        # run the simulation
        os.chdir(simPath)
        os.system("cgx -bg run.fbd")
        # extract frequencies
        os.system("../../Scripts/dat2txt.py " + ctyp)
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