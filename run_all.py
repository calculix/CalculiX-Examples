#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" © Ihor Mirzov, February 2020
Ctrl + F5 to Run all test scripts in the example collection """

import os
import sys
import fnmatch
import time
import shutil
import subprocess
import signal


# How many files to process
limit = 1000000

# Do not append 'quit' command to those files.
# They are read from other .fbd.
skip = ('shell.fbd',
        'solid.fbd',
        'post-modal.fbd',
        'values.fbd',
        'values.fbl',
        'geo.fbd',
        'shell-sym.fbd',
        'solid-sym.fbd',
        )

# Recursively list all .ext-files
# starting from 'start_folder'
def scan_all_files_in(start_folder, ext):
    all_files = []
    for f in os.scandir(start_folder):
        if f.is_dir():
            for ff in scan_all_files_in(f.path, ext):
                all_files.append(ff)
        elif f.is_file() and f.name.endswith(ext):
            all_files.append(f.path)
    return sorted(all_files)[:limit]


# Append a command to all filtered files
def append_command(start_folder, filtr, command):

    # Generate file list
    counter = 0
    flist = []
    for path, dirs, files in os.walk(start_folder):
        for filename in fnmatch.filter(files, filtr):
            counter = counter + 1
            ffile = os.path.join(path, filename)
            relpath = os.path.relpath(ffile, os.path.dirname(__file__))
            if not os.path.basename(ffile) in skip:
                flist.append(ffile)

    # Process each file
    rflist = []
    for ffile in flist:

        # Read file contents
        lines = []
        with open(ffile, 'r') as f:
            lines = f.readlines()

        # Get last non empty line
        i = len(lines) - 1
        last_line = lines[i].strip()
        while not len(last_line):
            lines.pop(i)
            i -= 1
            last_line = lines[i].strip()

        # Write command to end of file
        if last_line != command:
            lines.append('\n' + command + '\n')
            rflist.append(ffile)
        with open(ffile, 'w') as f:
            f.writelines(lines)

    return rflist


# Erase appended command from each of file in flist
def erase_command(flist, command):
    for ffile in flist:

        # Read file contents
        lines = []
        with open(ffile, 'r') as f:
            lines = f.readlines()

        # Get last non empty line
        i = len(lines) - 1
        last_line = lines[i].strip()
        while not len(last_line):
            lines.pop(i)
            i -= 1
            last_line = lines[i].strip()

        # Remove last command from the end of file
        if last_line == command:
            lines.pop(i)

        # Remove last empty line in the end of file
        if lines[len(lines) - 1].strip() == '':
            lines.pop(len(lines) - 1)

        # Save file
        with open(ffile, 'w') as f:
            f.writelines(lines)


# Run all tests
def run_all_tests_in(start_folder):
    start = time.perf_counter() # start time

    # Run tests
    counter = 0
    for file_name in scan_all_files_in(start_folder, 'test.py'):
        counter += 1
        relpath = os.path.relpath(file_name, start=os.path.dirname(__file__))
        print('\n{}\n{}: {}'
            .format('='*50, counter, relpath))

        # Change to the example directory
        os.chdir(os.path.dirname(file_name))

        # Execute the test script
        start2 = time.perf_counter() # start time
        os.system('./test.py > test.log')
        os.chdir(start_folder)
        print('{:.1f} seconds'\
            .format(time.perf_counter() - start2))

        # Kill gv windows after cgx graph command
        kill_gv('gs')
        kill_gv('gv')

    print('Total {:.1f} seconds\n'\
        .format(time.perf_counter() - start))


# Kill gv windows after cgx graph command
def kill_gv(name):
    try:
        plist = subprocess.check_output(['pidof', name])
        plist = plist.strip().decode().split()
        for pid in plist:
            os.kill(int(pid), signal.SIGKILL)

    # No such process
    except:
        pass


# Check relpath from example folder to Scripts
def check_rel_path(start_folder, scripts_dir, mask):
    counter = 1
    for file_name in scan_all_files_in(start_folder, mask):

        # Relative path from test.py to Scripts folder
        relpath1 = os.path.relpath(scripts_dir,
            start=os.path.dirname(file_name))

        # Relative path to test.py
        relpath2 = os.path.relpath(file_name, start=os.curdir)

        print('\n{}: {}\n'
            .format(counter, relpath2))
        counter += 1

        # Check relpath in test.py code
        OK = True
        with open(file_name, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line.startswith('sys') and 'Scripts' in line:
                    command = line[4:].split()[0]
                    if not os.path.dirname(command) == relpath1:
                        print('ERROR', relpath1, command)
                        OK = False
        if OK:
            print('OK')


if __name__ == '__main__':
    start_folder = os.path.dirname(__file__)
    scripts_dir = os.path.join(start_folder, 'Scripts')

    """
    # Modify PATH to provide access to the helper scripts
    if not scripts_dir in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + scripts_dir
    print('\nPATH = {}\n'.format(os.environ['PATH']))
    """

    """
    # Check relpath from example folder to Scripts
    check_rel_path(start_folder, scripts_dir, 'test.py')
    check_rel_path(start_folder, scripts_dir, '.fbd')
    check_rel_path(start_folder, scripts_dir, '.fbl')
    """

    # Modify files for windows autoclose
    flist1 = append_command(start_folder, '*.fbd', 'quit')
    flist2 = append_command(start_folder, '*.fbl', 'quit')
    flist3 = append_command(start_folder, '*.geo', 'Exit;')
    erase_command(['Scripts/monitor.py'], 'pylab.show()')

    # Run all tests
    run_all_tests_in(start_folder)

    # Roll back files modifications
    erase_command(flist1, 'quit')
    erase_command(flist2, 'quit')
    erase_command(flist3, 'Exit;')
    append_command('./Scripts', 'monitor.py', 'pylab.show()')

    """
    # Unusual test.py files
    # ./Thermal/Thermal distortion/test.py
    # ./Drahtbiegen/Biegung/test.py
    # ./Contact/Shell0/test.py
    # ./Pillow/test.py
    """
