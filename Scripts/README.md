# Helper Scripts
These scripts augment the automation capabilities of CGX.

File                        | Contents    
 :-------------             | :-------------
 [dat2txt.py](dat2txt.py)   | Extract time history and frequency data from DAT files     
 [monitor.py](monitor.py)   | Create convergence plots based on the CVG and STA files
 [param.py](param.py)       | Preprocessor for python expressions in arbitrary files
 [periodic.py](periodic.py) | Preprocessor to generate periodic boundary conditions for brick-shaped RVE meshes
 [separate.py](separate.py) | Preprocessor to split an existing mesh such that no node is used by more than one element. Continuity is enforced by equations instead. Purpose: Avoid nodal averaging of results.

## Setup

The example docs assume that the helper scripts are found in the PATH. See [Setup](../Setup.md) for instructions how to do this.

## dat2txt.py

 This script extracts arbitrary result items from a given DAT file to an easy to parse tabular text file with one line per time point. Currently, this works for output requested by
 + `*node print`
 + `*el print`
 + `*section print`.
 + frequency steps (no particular output command required)


 ```
> dat2txt.py [<jobname>]
 ```  
This reads `<jobname>.dat` and writes a text file for each result item in the DAT file. The names (without extension .txt) are printed to the console.

If no jobname is given, the current directory is searched for any DAT file and if a single one is found, it is used.

If multiple DAT files are found, their names are printed and no processing is done.

This means: If you have just a single DAT file in your directory, it is sufficient to call the script without parameters:
 ```
> dat2txt.py
No jobname given.
Found  solve.dat
total force fx,fy,fz_NKW
>
 ```  

For example, the DAT-file might contain these lines:
```
forces (fx,fy,fz) for set NROT and time  0.2000000E-01

        2 -1.323856E-16 -9.342657E-01  9.120891E-18

total internal energy for set EDRAHT and time  0.2000000E-01

       2.153755E-03

forces (fx,fy,fz) for set NROT and time  0.4000000E-01

        2 -1.520904E-14  3.031209E+01  5.927751E-16

total internal energy for set EDRAHT and time  0.4000000E-01
```
The script recognizes the items and creates the following text files:
* `forces (fx,fy,fz)_NROT.txt`
* `total internal energy_EDRAHT.txt`

The first column contains the time values and all available data for that item and time point is stored in the subsequent columns. For example, this is the content of `forces (fx,fy,fz)_NROT.txt`:
```
0.02          2 -1.323856E-16 -9.342657E-01  9.120891E-18
0.04          2 -1.520904E-14  3.031209E+01  5.927751E-16
```

Frequency outout is written to separate text files:
+ `Eigenvalues_<nr>.txt` eigenvalues, `<nr>` is a counter.
+ `Eigenvalues_PF_<nr>.txt` participation factors.
+ `Eigenvalues_MM_<nr>.txt` modal masses.

Examples:
* [Drahtbiegen/Biegung/](../Drahtbiegen/Biegung/)
* [NonLinear/3PB/](../NonLinear/3PB/)

## monitor.py

This script reads the STA and CVG files for a given job and creates an image with two diagrams:

* force residuals, displacement correction and incremental time step ,
* step time and number of contact elements.

```
> monitor.py [<jobname>]
```
Specification of the jobname is only required if
there is more than one STA file in the current directory.

The plot is displayed and written to `<jobname>.png`.

Examples:
* [Drahtbiegen/Biegung/](../Drahtbiegen/Biegung)
* [Pillow/](../Pillow/)
* [Kasten/](../Kasten/)
* [NonLinear/3PB/](../NonLinear/3PB/)

## param.py

This script allows you to parametrize text files. Parametrization means that
you replace literal values (strings or numeric values) in text files by
expressions. These expressions can contain variables, which can be defined at
the beginning (or elsewhere in the file) and can be referenced wherever below
their definition.

Definitions in the file can be overridden from the command line.

### Usage

* Copy the file to be parametrized to `<filename>.par` or (better) `par.<filename>`, where `<filename>` can include any extension. This will become the source file for parametrization.

  Prefixing with `par.` is recommended, as this does not spoil the syntax highlighting in editors and you can call `param.py` without specifying the file name if there is just one such file in the current directory.

* In `<filename>.par` or `par.<filename>` add parameter definitions, preferably in comment lines.   
  * To assign the value 4 to the variable a, include `<a=4>` to such a line.
  * To reference the value just add `<a>` wherever the value has to go.
  * Wherever you need a value depending on a, write something like `<b=a^2>` or
   `<-a>`. If you want floating point results, make sure to use floating point
   variables or values (with a period. eg. `<a=2.>`).
* To extract a usable file `<filename>`, run
```
> param.py <filename>.par
```
or (depending on your choice for source naming)
```
> param.py [par.<filename>]
```
If the filename starts with `par.` and only one such file is present in the directory, then it is sufficient to just call
```
> param.py
```

The expressions are scanned and the angle brackets
replaced (pre-processing):
  * Variable definitions are copied verbatim to the output (for reference/documentation).   
  * Expressions are replaced by their result.
  * Python expressions involving the following functions from the `math` module can be used:
  ```
  'acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'log',
  'log10', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'
  ```
  * The following built-ins are unlocked for usage in expressions:
  ```
  'abs', 'int'
  ```


|                 | `<filename>.par` or `par.<filename>` |`<filename>` |
|  :------------- | :-------------   |:--          |
|  Definitions    | `<a=2>`          |`a=2`        |
|                 | `<b=2*a>`        |`b=2*a`      |
|                 | `<type="he8">`   | `type=”he8”`|
|  Expression     | `<a>`            | `2`         |
|                 | `<2*a>`          | `4`         |
|                 | `<b>`            | `4`         |
|                 | `<a+b>`          | `6`         |
|                 | `<type>`         | `he8`       |
|                 | `<sqrt(2)>`      | `1.414...`  |
|                 | `<pi/2>`         | `1.57...`   |

### Overriding parameter values from the command line

You can override definitions in the file from the command line using additional command line parameters of the form `name=value` just like you would write in the `<...>` tags in the file.
Definitions from the command line take precedence to whatever assignments to the variable `name` within the file.
```
> param.py par.<filename> <name1>=<value1> <name2>=<value2>
```
This feature is designed to support script-controlled parametric studies without the need to edit the parameter definitions inside the files.

### param.py vs. CGX valu

CGX supports parametrization starting with version 2.7 (see the `valu` command).

Advantages of param.py over CGX valu
* Works with older CGX versions
* Non-CGX-files can be parametrized (e.g. CCX input)
* More natural expressions (CGX has reversed polish notation)
* Large variety of available python functions
* Parameter override from the command line

Disadvantages:
* Extra pre-processing step required
* Static replacement before use of the File (e.g. no access to the stack or to result values in postprocessing)

Examples:
* [Drahtbiegen/Zug/](../Drahtbiegen/Zug/)
* [Thermal/Thermal distortion/](../Thermal/Thermal%20distortion/)
* [Linear/StressConc1/](../Linear/StressConc1/)
* [NonLinear/3PB/](../NonLinear/3PB/)

## periodic.py

This script creates equations for periodic boundary conditions of a
brick-shaped RVE, specified by a mesh file with at least the `*node` definitions.
We assume that it's corners are at (0,0,0) and (lx,ly,lz).
The dimensions are determined from the nodal co-ordinates.
```
> periodic.py <meshfile>
```  
The console output of the script shows
- the file used,
- the dimensions of the RVE
- the numbers of the control nodes
- the amount of nodes eliminated by periodicity.

This is the output in example [RVE/Periodic/](../RVE/Periodic/)
```
Using file: all.msh
lx: 1.0
ly: 1.0
lz: 1.0
n0: 1321
nx: 1211
ny: 221
nz: 1331
332 nodes constrained
```
The average deformation gradient of the RVE corresponds to the displacements of
the control nodes. These can be specified using `*boundary`.

## separate.py

This script enable the display of results not averaged at the nodes in CGX. The
trick is to provide a separate node for each element where otherwise all adjacent
elements would share the same node. Instead of ensuring continuity of the
displacement field by using the same node, identical displacement of
repeated nodes is enforced using equations.

These equations completely eliminate the dofs of the added nodes, such that no
further input modificiation is required.
```
> separate.py <meshfile>
```  
The console output of the script shows
- the file used,
- the element type, number of nodes and number of dofs per element for
all `*element` blocks

The script produces three files
- `separate-nod.inc`: Nodes of the separated meshes. This includes the original and the duplicated nodes.
- `separate-ele.inc`: Elements of the separated meshes. Node numbers are modified as required.
- `separate-eqn.inc`: Equations to enforce continuity.

In order suppress the nodal averaging for an existing CCX input file, replace the mesh by
```
*include,input=separate-nod.inc
*include,input=separate-ele.inc
*include,input=separate-eqn.inc
```

No other changes need to be made, as all set definitions remain valid.

Limitations:
- No in-depth tests performed (just the example [../Linear/Separate](../Linear/Separate))
- Nodes and elements of the original mesh must reside in a single file (typcially `all.msh` from CGX)
- No effect on multilayer shell elements in through-thickness direction

For hexahedral meshes, the amount of nodes (and thus the size of the results file) can grow by a factor of 8. The number of dofs, however, remains the same, as all added nodes are eliminated by equations.
