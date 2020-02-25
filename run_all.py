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


# Run examples automatically closing windows
class RunAllTests:


    # Initialization
    def __init__(self, limit, start_folder):
        self.limit = limit
        self.start_folder = start_folder
        self.home = os.path.dirname(__file__)
        self.scripts_dir = os.path.join(self.home, 'Scripts')

        # Do not append 'quit' command to those files.
        # They are read from other .fbd.
        self.skip = (
            'shell.fbd',
            'solid.fbd',
            'post-modal.fbd',
            'values.fbd',
            'values.fbl',
            'geo.fbd',
            'shell-sym.fbd',
            'solid-sym.fbd',
            )


    # Append a command to all filtered files
    def append_command(self, folder, filtr, command):

        # Generate file list
        counter = 0
        flist = []
        for path, dirs, files in os.walk(folder):
            for filename in fnmatch.filter(files, filtr):
                counter = counter + 1
                ffile = os.path.join(path, filename)
                relpath = os.path.relpath(ffile, self.home)
                if not os.path.basename(ffile) in self.skip:
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
    def erase_command(self, flist, command):
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


    # Recursively list all .ext-files
    # starting from 'start_folder'
    def scan(self, start_folder, ext):
        all_files = []
        for f in os.scandir(start_folder):
            if f.is_dir():
                for ff in self.scan(f.path, ext):
                    all_files.append(ff)
            elif f.is_file() and f.name.endswith(ext):
                all_files.append(f.path)
        return sorted(all_files)[:self.limit]


    # Kill gv windows after cgx graph command
    def kill_gv(self, name):
        try:
            plist = subprocess.check_output(['pidof', name])
            plist = plist.strip().decode().split()
            for pid in plist:
                os.kill(int(pid), signal.SIGKILL)

        # No such process
        except:
            pass


    # Check relpath from example folder to Scripts
    def check_rel_path(self, start_folder, scripts_dir, mask):
        counter = 1
        for file_name in self.scan(start_folder, mask):

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


    # Run all tests
    def run(self):
        counter = 0
        all_tests = self.scan(self.start_folder, 'test.py')
        for file_name in all_tests:
            start = time.perf_counter() # start time
            dir_name = os.path.dirname(file_name)
            counter += 1
            relpath = os.path.relpath(file_name, start=self.home)
            print('\n{}\n{}: {}'
                .format('='*50, counter, relpath))

            # Modify files for windows autoclose
            flist1 = self.append_command(dir_name, '*.fbd', 'quit')
            flist2 = self.append_command(dir_name, '*.fbl', 'quit')
            flist3 = self.append_command(dir_name, '*.geo', 'Exit;')
            monitor_py = os.path.join(self.scripts_dir, 'monitor.py')
            self.erase_command([monitor_py], 'pylab.show()')

            # Execute the test script
            os.chdir(dir_name)
            os.system('./test.py > test.log')
            os.chdir(self.start_folder)

            # Roll back files modifications
            self.erase_command(flist1, 'quit')
            self.erase_command(flist2, 'quit')
            self.erase_command(flist3, 'Exit;')
            self.append_command(self.scripts_dir, 'monitor.py', 'pylab.show()')

            # # Check relpath from example folder to Scripts
            # self.check_rel_path(self.start_folder, self.scripts_dir, 'test.py')
            # self.check_rel_path(self.start_folder, self.scripts_dir, '.fbd')
            # self.check_rel_path(self.start_folder, self.scripts_dir, '.fbl')

            # Kill gv windows after cgx graph command
            self.kill_gv('gs')
            self.kill_gv('gv')

            # Time spent
            print('{:.1f} seconds'\
                .format(time.perf_counter() - start))


if __name__ == '__main__':
    start = time.perf_counter() # start time

    # This will run all examples
    start_folder = os.path.dirname(__file__)
    limit = 1000000 # how many files to process

    # # This will run one example only
    # start_folder = os.path.dirname(__file__) \
    #     + '/Elements/Solid'
    # limit = 1 # how many files to process

    auto = RunAllTests(limit, start_folder)
    auto.run()

    # Time spent
    delta = time.perf_counter() - start
    print('\nTotal {:02d}:{:02d}:{:02.0f}'\
        .format(int(delta/3600), int(delta%3600/60), delta%3600%60))
