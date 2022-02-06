# CalculiX-Examples - Setup

Working environment:

+ Example files
+ Command window (terminal) with the following commands working:
  + `python` either python 2 or python 3 for the helper scripts
  + `monitor.py`, `dat2txt.py`, `param.py`, `periodic.py`, `separate.py` (helper scripts from the examples collection)
  + `gmsh` (sometimes used for geometry and meshing)
  + `join`, `mv` (unix commands, under Windows you might install Cygwin to make them available)
  + `gnuplot` (plotting program)
  + `cgx` and `ccx` (the CalculiX programs)
  + `git` (source code management system, for easy update of the example collection)
  + `tetgen` (tetgen tetraeder mesher)
  + `cgxCadTools` based on Open CASCADE Technology

The examples are developed under Linux but most of them might work under Windows.

### Example files (Windows and Linux)

On the main page there is a button `Clone or download` You can
+ Copy the Git link to the repository to the clipboard or
+ Download a zip file containing the complete example directory structure

Unpack/install the files to a directory (called `<exampledir`)

+ where you have read and write access
+ with fast read and write access (not on a network or slow portable drive)
+ with 2 GB free disk space if you want to run all examples (that might increase in future, by February 2022, 1,6 GB MB are
  used)

File types

| Extension   | Type                    | Support in SciTE | Support in Atom | Support in VSCode
| :--         | :--                     | :--              | :--             | :-- 
| `.fbd .fbl` | CGX  pre/post scripts   | x                | x               | 
| `.inp`      | CCX solver input        | x                | x               | x
| `.geo`      | Gmsh input              | x                | x               | x
| `.gnu`      | Gnuplot script          | x                |                 | x
| `.py`       | Python script           | x                | x               | x
| `.md`       | Markdown (documentation)|                  | x               | x

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

Under Windows, I recommend the [bConverged](http://bconverged.com/) build. It has nice SciTE integration with syntax highlighting and execution hotkeys for various relevant file types. However, it is out of maintenance since version 2.10. 

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

Originally, all examples were developed and tested with CalculiX 2.10 in the virtual box provided by Kai Kaß¢ohm at [fiziko.de](http://www.fiziko.de/vbox/). It is is not available any more.

For editing CGX, CCX  or gmsh input under linux, I recommend [atom](https://atom.io/), it has syntax highlighting for these files and markdown preview.

An alternative is Visual Studio Code, which, however, has no language support for CGX input files.

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
