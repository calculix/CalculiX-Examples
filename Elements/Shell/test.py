#!/usr/bin/env python

""" Convergence study for solid elements """

import os
import multiprocessing
import matplotlib.pyplot as plt
import numpy
import shutil


# Provide access to the helper scripts
def modify_path():
    scripts_dir = os.path.dirname(__file__)
    while not 'Scripts' in os.listdir(scripts_dir):
        scripts_dir = os.path.abspath(os.path.join(scripts_dir, '..'))
    scripts_dir = os.path.join(scripts_dir, 'Scripts')
    if not scripts_dir in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + scripts_dir
    print('\nPATH = {}\n'.format(os.environ['PATH']))


# Runs a convergence study
def shell_conv():
    # Calculix solid element types with their cgx counterparts
    eltyps={"S3":"tr3u",
        "S4":"qu4",
        "S4R":"qu4r",
        "S6":"tr6u",
        "S8":"qu8",
        "S8R":"qu8r"}

    #elsizes=[50,20,10,5]
    # C3D4 mesh fails for those elsize
    #elsizes=[500,250,100,50,25,10,5]
    elsizes=[100,50,25,10,5]

    # read the template fbd file
    f = open("shell.fbd","r")
    lines=f.readlines()
    f.close()
    # loop over element types
    for elty in eltyps.keys():
        # open results summary file
        fdata=open(elty+".txt","w")
        fdata.write("# size NoN smax umax\n")
        # loop over element sizes
        for elsize in elsizes:
            print(elty, elsize)
            # modify shell.fbd and write output to shell-auto.fbd
            fout = open("shell_auto.fbd", "w")
            for line in lines:
                # set element type
                if line.startswith("valu Etyp"):
                    line="valu Etyp "+eltyps[elty]+"\n"
                    # set element size
                if line.startswith("div all auto"):
                    line="div all auto "+str(elsize)+"\n"
                    if elty.startswith("S3") or elty.startswith("S4"):
                        # increase the node distance for linear elements
                        line=line+"div all div 2\n"
                        elsize=elsize*2
                    fout.write("ulin "+elty+" "+str(elsize)+"\n")
                fout.write(line)
            fout.write("quit\n")
            fout.close()
            # run shell_auto.fbd (preprocessing, solving and postprocessing)
            os.system("cgx -b shell_auto.fbd")
            # get number of nodes from solid.frd
            f=open("shell.frd")
            for line in f:
                if line.startswith("    2C"):
                    nnode=int(line.split()[1])
            f.close()
            print("Knotenzahl ", nnode)
            # get smax from smax.txt
            smax=numpy.genfromtxt("smax.txt")[3]
            # get umax from umax.txt
            smin=numpy.genfromtxt("smin.txt")[3]
            # get umax from umax.txt
            umax=numpy.genfromtxt("umax.txt")[3]
            # rename the stress plot
            os.system("mv hcpy_1.png "+"shell_"+elty+"_"+str(elsize)+"_S.png")
            # write the values to the data file
            fdata.write(str(elsize)+" "+str(nnode)+" "+str((smax-smin)/2.)+" "+str(abs(umax))+"\n")
        fdata.close()


# Plots the results of a convergence study
def shell_plot():
	# reference values, see smath sheet
	sref=1.848
	wref=0.0587
	# List of the element types to process (text files)
	eltyps=["S3",
		"S4",
		"S4R",
		"S6",
		"S8",
		"S8R"]
	plt.figure(figsize=(10, 5.0), dpi=100)
	plt.subplot(1,2,1)
	plt.title("Stress")
	# plt.hold(True) # deprecated
	for elty in eltyps:
		data = numpy.genfromtxt(elty+".txt")
		plt.plot(data[:,1],data[:,2]/sref,"o-")
	plt.xscale("log")
	plt.xlabel('Number of nodes')
	plt.ylabel('Max $\sigma / \sigma_{\mathrm{ref}}$')
	plt.grid(True)
	plt.subplot(1,2,2)
	plt.title("Displacement")
	# plt.hold(True) # deprecated
	for elty in eltyps:
		data = numpy.genfromtxt(elty+".txt")
		plt.plot(data[:,1],data[:,3]/wref,"o-")
	plt.xscale("log")
	plt.xlabel('Number of nodes')
	plt.ylabel('Max $u / u_{\mathrm{ref}}$')
	plt.ylim([0,1.2])
	plt.grid(True)
	plt.legend(eltyps,loc="lower right")
	plt.tight_layout()
	plt.savefig("shell.svg",format="svg")
	plt.show()


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
    os.system("")
    shell_conv()
    shell_plot()
    #move(snap)
