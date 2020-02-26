# CalculiX-Examples - Setup

Working environment:

+ Example files
+ Command window (terminal) with the following commands working:
  + `monitor.py`, `dat2txt.py`, `param.py`, `periodic.py`, `separate.py` (helper scripts from the examples collection)
  + `gmsh` (sometimes used for geometry and meshing)
  + `join`, `mv` (unix commands, under Windows you might install Cygwin to make them available)
  + `gnuplot` (plotting program)
  + `cgx` and `ccx` (the CalculiX programs)
  + `git` (source code management system, for easy update of the example collection)
  + `ng_vol` (netgen tetraeder mesher)
  + `cgxCadTools` based on Open CASCADE Technology

The examples are developed under Linux but most of them might work under Windows.

### Example files (Windows and Linux)

On the main page there is a button `Clone or download` You can
+ Copy the Git link to the repository to the clipboard or
+ Download a zip file containing the complete example directory structure

Unpack/install the files to a directory (called `<exampledir`)

+ where you have read and write access
+ with fast read and write access (not on a network or slow portable drive)
+ with 500 MB free disk space (that might increase in future, by end of June 1016, 250 MB are
  used)

File types

| Extension | Type                    | Support in SciTE | Support in Atom |
| :--       | :--                     | :--              | :--             |
| `.fbd .fbl` | CGX  pre/post scripts | x                | x               |
| `.inp`    | CCX solver input        | x                | x               |
| `.geo`    | Gmsh input              | x                | x               |
| `.gnu`    | Gnuplot script          | x                |                 |
| `.py`     | Python script           | x                | x               |
| `.md`     | Markdown (documentation)|                  | x               |

### Windows Setup

Windows is not the native development platform for CalculiX and this may cause problems at any time. Some of them are:

+ CCX fails to clean the result files upon startup if the files (e.g. .frd) is still open in CGX. Thus, the .frd file accumulates the results of multiple runs instead of just being re-written.
+ CGX doesn't properly syncronize screen shots with `hcpy`. The command acts as if it was written some commands further above in the .fbd file.

Don't expect all system calls (`sys` command) in the CGX scripts to work. In particular:
+ Many examples use the unix command `mv` to rename files (screenshots, results)
+ Some examples use `join` to combine results files, mainly to create force-displacement plots.
Former problems with incompatible `echo` behaviour have been fixed.

#### Helper Scripts

Running the helper scripts requires a Python installation with the matplotlib package available. You may need to install this package using
```
>pip install matplotlib
```
#### CalculiX

Under Windows, I recommend the [bConverged](http://bconverged.com/) build. It has nice SciTE integration with syntax highlighting and execution hotkeys for various relevant file types.

If you are not familiar with this distribution, the
[GettingStarted Tutorial](http://bconverged.com/content/calculix/doc/GettingStarted.pdf) is recommended.

The distribution comes with a pre-configured command line window (console), where you can execute the commands given in the example documentation. To start the console: **Start> Programs> bConverged> CalculiX> CalculiX Command**

It might be convenient to add a desktop link to the CalculiX command window.

Customize the bConverged CalculiX startup script by editing the file `%CALCULIX_ROOT%\common\site\cmdStartup.bat`. To provide access to the helper scripts, add the `<exampledir>\Scripts` directory to your path, e.g. by adding a line next to the other set commands:
```
set PATH=<exampledir>\Scripts;%PATH%
```
`<exampledir>` might be something like `D:\FHB\Software\CalculiX\Git`.

You might also wish to change the default working directory (default current directory in the CalculiX command window).

Run the examples in the CalculiX Command Window.

The [CalculiX homepage](http://www.dhondt.de/) provides Windows binaries of the newest version. You can use these to update the corresponding files in the bConverged distribution.

#### Other Tools

**Gnuplot** is already included in the bConverged CalculiX distribution.

**Gmsh** is only included if you purchase the Open Engineering Suite from bConverged.

Otherwise you can install it separately from http://gmsh.info/.
Make sure that the executable is in the path.

**Markdown Editor** For viewing the README.md files (or for writing your own), you might install [Markdown Edit](http://markdownedit.com/). It has life preview with support for Github flavoured Markdown (except for tables, these aren't rendered).

Open the README.md in `<exampledir>` with MarkdownEdit and click the preview images to open the  corresponding example subdirectory in a file manager window.

#### GE Distribution

If you use the [GE distribution of CalculiX](https://github.com/GeneralElectric/CalculiX), the
right spot to modify the path variables is
`<GEhome>\etc\CalculiXWindowsEnvironment.bat`. Add these settings:
```
set PROJECT=<exampledir>
set PATH=%PROJECT%\Scripts;%PATH%
```
You should run the examples in the CalculiXWindowsShell, provided with the distribution.

### Linux Setup

All examples are developed and tested with CalculiX 2.10 in the virtual box provided by Sven Kaßbohm at [fiziko.de](http://www.fiziko.de/vbox/). It is configured such that you can easily compile new versions of CCX and CCX.

Python, Gmsh and Gnuplot are included.

For tetraeder meshing of solid parts netgen is called by CGX. The binary file `ng_vol` must be in the path. See [ngsolve.org](https://ngsolve.org/downloads) for instructions on download and installation.

It has, however, some disadvantages:

* Hardware Open GL does not work
* Multithreading does not work.
* Avoid working in folders shared with the host system.

These are not relevant for simple educational models but are definitely relevant for serious work.

For editing CGX, CCX  or gmsh input under linux, I recommend [atom](https://atom.io/), it has syntax highlighting for these files and markdown preview.

#### Helper Scripts

`<exampledir` might be `$HOME/GIT/CalculiX-Examples`.
Add the following line to your `.bashrc`:
```
export PATH="<exampledir>/Scripts:$PATH"
```
CGX executes sys commands in sh, not in the bash. As the scripts also are called from CGX scripts, you have to augment the path for sh as well by adding this to your `.profile`:
```
PATH="<exampledir>/Scripts:$PATH"
```
