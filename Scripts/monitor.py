#!/usr/bin/python
"""
This is a monitor for .sta and .cvg files of calculix
"""
import sys
import pylab
import numpy
import glob

# print sys.argv[1]
# job = sys.argv[1]
# processing command line arguments, get the
# jobname
if len(sys.argv)==1:
    print "No jobname given."
    files=glob.glob("*.sta")
    if len(files)==1:
        print "Found", files[0]
        job=files[0][:-4]
    else:
        print "Available .sta files:"
        for f in files:
            print "  ", f
        quit()
if len(sys.argv)>1:
    print "Jobname:",sys.argv[1]
    job = sys.argv[1]

sta=numpy.genfromtxt(job+'.sta',skip_header=2,delimiter=[6,11,7,6,14,14,14])
cvg=numpy.genfromtxt(job+'.cvg',skip_header=4)
# ensure 2dim array in case of single data line
if sta.ndim==1:
    sta=sta[numpy.newaxis,:]
"""
.sta
 0 STEP
 1 INC
 2 ATT
 3 ITRS
 4 TOT TIME
 5 STEP TIME
 6 INC TIME
 .cvg
 0 STEP
 1 INC
 2 ATT
 3 ITER
 4 CONT EL
 5 RESID FORCE
 6 CORR DISP
 7 RESID FLUX
 8 CORR TEMP"""
# iteration counter
iters=cvg.shape[0]  # number of iterations
it=range(iters)     # range for loop over iterations
# increment number for iteration
itinc=cvg.astype(int)[:,1]    # increment number for the iterations
itstep=cvg.astype(int)[:,0]   # step number for the iteration
itdt=numpy.empty([iters])     # time step for the iteration
itsteptime=numpy.empty([iters])  # Step time for iterations
for i in it:
    stp = itstep[i]
    inc = itinc[i]
	# ccx writes values below 1e-6 as zero
    if (cvg[i,5]==0.0):
        cvg[i,5]=0.5
    for j in range(sta.shape[0]):
        if (stp==sta.astype(int)[j,0]) and (inc==sta.astype(int)[j,1]):
            itdt[i]=sta[j,6]
            itsteptime[i]=sta[j,5]
            print i, stp, inc, j, itdt[i],itsteptime[i],cvg[i,5]
            imax=i
## Plot force residuals, disp correction and time step
pylab.subplot(2,1,1)
pylab.title('sta and cvg data of job '+job )
pylab.semilogy(it[:imax],itdt[:imax],'-',
               it[:imax],cvg[:imax,5],'-',
               it[:imax],cvg[:imax,6],'r-')
pylab.grid()
pylab.legend(['dt','force','disp'],
             fontsize='small',framealpha=0.5, loc=2)
# step time and number of contact elements
sp1=pylab.subplot(2,1,2)
pylab.plot(it[:imax],itsteptime[:imax],'r-',
           it[:imax],itsteptime[:imax],'b-',)
pylab.legend(['# cont. el.','step time'],
             fontsize='small',framealpha=0.5, loc=2)
pylab.ylabel('step time')
pylab.xlabel('Iteration')
pylab.grid()
sp2=sp1.twinx()
pylab.plot(it[:imax],cvg[:imax,4],'r-')
pylab.ylabel('# of cont. elements')
pylab.savefig(job)
pylab.show()
