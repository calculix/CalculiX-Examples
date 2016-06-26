# CalculiX-Examples - Setup

Working environment:

+ Example files
+ CalculiX (CGX and CCX)
+ Setup of the path to the helper scripts
+ Gmsh (sometimes used for geometry and meshing)
+ Git (for convenient and smart update of the example files)

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

#### CalculiX

Under Windows, I recommend the [bConverged](http://bconverged.com/) build. It has nice SciTE integration with syntax highlighting and execution hotkeys for various relevant file types.

If you are not familiar with this distribution, the
[GettingStarted Tutorial](http://bconverged.com/content/calculix/doc/GettingStarted.pdf) is recommended.

The distribution comes with a pre-configured command line window (console), where you can execute the commands given in the example documentation. To start the console: **Start> Programs> bConverged> CalculiX> CalculiX Command**

It might be convenient to add a desktop link to the CalculiX command window.

#### Helper Scripts

Running the helper scripts requires a Python installation with the matplotlib package available. You may need to install this package using
```
>pip install matplotlib
```
Customize the CalculiX startup script by editing the file `%CALCULIX_ROOT%\common\site\cmdStartup.bat`. To provide access to the helper scripts, add the `<exampledir>\Scripts` directory to your path, e.g. by adding a line next to the other set commands:
```
set PATH=<exampledir>\Scripts;%PATH%
```
`<exampledir>` might be something like `D:\FHB\Software\CalculiX\Git`.

You might also wish to change the default working directory (default current directory in the CalculiX command window).

Don't expect all system calls (`sys` command) in the CGX scripts to work. Normally, there should be windows equivalents but tests mainly have been done  under Linux.

#### Other Tools

**Gnuplot** is already included in the bConverged CalculiX distribution.

**Gmsh** is only included if you purchase the Open Engineering Suite from bConverged.

Otherwise you can install it separately from http://gmsh.info/.

**Markdown Editor** For viewing the README.md files (or for writing your own), you might install [Markdown Edit](http://markdownedit.com/). It has life preview with support for Github flavoured Markdown.

Open the README.md in `<exampledir>` with MarkdownEdit and click the preview images to open the  corresponding example subdirectory in a file manager window.

### Linux Setup

All examples are developed and tested with CalculiX 2.10 in the virtual box provided by Sven Kaßbohm at [fiziko.de](http://www.fiziko.de/vbox/). It is configured such that you can easily compile new versions of CCX and CCX.

Python, Gmsh and Gnuplot are included.

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
