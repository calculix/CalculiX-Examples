#!/usr/bin/env python
"""
This is a monitor for .sta and .cvg files of calculix
Updates the plot periodically while the job is still running.
"""
import sys
import time
import warnings
import subprocess
import platform
import matplotlib.pyplot as plt
import numpy
import glob

# print sys.argv[1]
# job = sys.argv[1]
# processing command line arguments, get the
# jobname and optional refresh interval (seconds, default 10)
if len(sys.argv)==1:
    print("No jobname given.")
    files=glob.glob("*.sta")
    if len(files)==1:
        print("Found", files[0])
        job=files[0][:-4]
    else:
        print("Available .sta files:")
        for f in files:
            print("  ", f)
        quit()
if len(sys.argv)>1:
    print("Jobname:",sys.argv[1])
    job = sys.argv[1]

interval = 10.0
if len(sys.argv)>2:
    interval = float(sys.argv[2])
print("Refresh interval:", interval, "s (Ctrl+C to stop)")

# Name des ccx-Prozesses, wie er im Task-Manager (Windows) bzw. "ps"/"pgrep"
# (Linux/Mac) auftaucht - unter Windows meist mit ".exe", unter Linux/Mac ohne.
CCX_EXE = 'ccx.exe' if platform.system()=='Windows' else 'ccx'

def job_running(exe_name=CCX_EXE):
    """Check whether a ccx process is currently running. Uses 'tasklist' on
    Windows and 'pgrep' on Linux/Mac. Returns True/False, or None if the
    check itself failed (tool not found, permissions, ...) - in that case
    the caller should not assume anything about the job's status."""
    try:
        if platform.system()=='Windows':
            out = subprocess.check_output(
                ['tasklist', '/FI', 'IMAGENAME eq '+exe_name],
                text=True, stderr=subprocess.DEVNULL)
            return exe_name.lower() in out.lower()
        else:
            result = subprocess.run(['pgrep', '-x', exe_name],
                                     stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)
            return result.returncode==0
    except Exception:
        return None


def read_data(job):
    """Read the current .sta and .cvg files. Returns (sta, cvg) or
    (None, None) if the .cvg file cannot be parsed (e.g. ccx is
    mid-write)."""
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            sta=numpy.genfromtxt(job+'.sta',skip_header=2,delimiter=[6,11,7,6,14,14,14])
    except Exception:
        sta=numpy.zeros((0,7))
    if sta.ndim==1 and sta.size>0:
        sta=sta[numpy.newaxis,:]
    if sta.size>0:
        # ccx may be mid-write of the last line when we read it; such
        # partial lines parse as rows containing NaN, which would later
        # trigger "invalid value encountered in cast" when cast to int.
        # Drop them here, before that comparison happens.
        sta=sta[~numpy.isnan(sta).any(axis=1)]
    if sta.size==0:
        # before the first increment is completed, the sta-file is empty
        # (genfromtxt returns a 0-row array without raising an exception
        # in that case), so we fake some contents to not crash later
        sta=numpy.array([[  1.   ,   1.   ,   1.   ,  0   ,   0  ,   0  ,   0  ]])
    try:
        cvg=numpy.genfromtxt(job+'.cvg',skip_header=4)
    except Exception:
        # .cvg can be mid-write while ccx is running; just skip this refresh
        return None, None
    if cvg.size==0:
        # if the job is linear, cvg data is empty.
        return None, None
    # ensure 2dim array in case of single data line
    if sta.ndim==1:
        sta=sta[numpy.newaxis,:]
    if cvg.ndim==1:
        cvg=cvg[numpy.newaxis,:]
    return sta, cvg


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

def make_plot(job, sta, cvg):
    # iteration counter
    iters=cvg.shape[0]  # number of iterations
    it=range(iters)     # range for loop over iterations
    # increment number for iteration
    itinc=cvg.astype(int)[:,1]    # increment number for the iterations
    itstep=cvg.astype(int)[:,0]   # step number for the iteration
    itdt=numpy.empty([iters])     # time step for the iteration
    itsteptime=numpy.empty([iters])  # Step time for iterations
    istamax=0
    icvgmax=0
    for i in it:
        stp = itstep[i]
        inc = itinc[i]
        # ccx writes values below 1e-6 as zero,
        if (cvg[i,5]==0.0):
            cvg[i,5]=1.e-7

        found=0
        for j in range(sta.shape[0]):
            if (stp==sta.astype(int)[j,0]) and (inc==sta.astype(int)[j,1]):
                itdt[i]=sta[j,6]
                itsteptime[i]=sta[j,5]
                istamax=i
                icvgmax=i
                found=1
        if (not found==1):
            icvgmax=i

    plt.clf()
    ## Plot force residuals, disp correction and time step
    plt.subplot(2,1,1)
    plt.title('sta and cvg data of job '+job+'  (last update: '+time.strftime('%H:%M:%S')+')')
    plt.semilogy(it[:istamax],itdt[:istamax],'-',
                   it[:icvgmax],cvg[:icvgmax,5],'g-',
                   it[:icvgmax],cvg[:icvgmax,6],'r-')
    plt.grid()
    # enforce integer x ticks
    ax = plt.gca()
    ax.xaxis.get_major_locator().set_params(integer=True)
    plt.legend(['dt','force','disp'],
      fontsize='small',framealpha=0.5, loc=2)
    # step time and number of contact elements
    sp1=plt.subplot(2,1,2)
    plt.plot(it[:istamax],itsteptime[:istamax],'r-',
               it[:istamax],itsteptime[:istamax],'b-',)
    plt.legend(['# cont. el.','step time'],
                 fontsize='small',framealpha=0.5, loc=2)
    plt.ylabel('step time')
    plt.xlabel('Iteration')
    plt.grid()
    # enforce integer x ticks
    ax = plt.gca()
    ax.xaxis.get_major_locator().set_params(integer=True)
    sp2=sp1.twinx()
    plt.plot(it[:icvgmax],cvg[:icvgmax,4],'r-')
    plt.ylabel('# of cont. elements')
    plt.tight_layout()
    plt.savefig(job, bbox_inches='tight')


plt.ion()
fig = plt.figure()
clock_text = fig.text(0.99, 0.005, '', ha='right', va='bottom',
                       fontsize=8, color='gray')

# stop the loop cleanly if the plot window is closed by hand
stopped = {'flag': False}
def _on_close(event):
    stopped['flag'] = True
fig.canvas.mpl_connect('close_event', _on_close)

last_update = 0.0
running = None   # None = unknown, True/False once first checked
try:
    while not stopped['flag']:
        now = time.time()

        if now - last_update >= interval:
            running = job_running()
            sta, cvg = read_data(job)
            if cvg is not None:
                make_plot(job, sta, cvg)
                # plt.clf() inside make_plot wiped the old clock_text artist,
                # so it needs to be re-created after every full redraw
                clock_text = fig.text(0.99, 0.005, '', ha='right', va='bottom',
                                       fontsize=8, color='gray')
            last_update = now
            if running is False:
                print("ccx läuft nicht mehr - letzte Aktualisierung, dann Ende.")
                clock_text.set_text('now: '+time.strftime('%H:%M:%S')+'  [ccx beendet]')
                plt.pause(0.1)
                break

        status = {True:'läuft', False:'beendet', None:'?'}[running]
        clock_text.set_text('now: '+time.strftime('%H:%M:%S')+'  (ccx: '+status+')')
        # tick in short slices instead of one plt.pause(1), so Ctrl+C
        # gets noticed within ~0.1s instead of up to 1s
        for _ in range(10):
            if stopped['flag']:
                break
            plt.pause(0.1)
except KeyboardInterrupt:
    print("\nStopped monitoring (Ctrl+C).")

plt.close(fig)
print("Monitor beendet.")

