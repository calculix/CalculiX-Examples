# Helper Scripts
These scripts augment the automation capabilities of CGX.

File                    | Contents    
 :-------------         | :-------------
 [dat2txt.py](dat2txt.py)     | Extract time history data from .dat files     
 [monitor.py](monitor.py)   | Create convergence plots based on the .cvg and .sta files
 [param.py](param.py) | Preprocessor tor python expressions in arbitrary files

## Setup

The example docs assume that the helper scripts are found in the PATH. See [Setup](../Setup.md) for instructions how to do this.

## dat2txt.py

 This script extracts arbitrary result items from a given .dat file to an easy to parse tabular text file with one line per time point. Currently, this only works for result items with scope to a node or element set (not for contact results, as these cannot be scoped to sets).
 ```
> dat2txt.py [<jobname>]
 ```  
This reads `<jobname>.dat` and writes a text file for each result item in the .dat file. The names (without extension .txt) are printed to the console.

If no jobname is given, the current directory is searched for any .dat file and if a single one is found, it is used.

If multiple .dat files are found, their names are printed and no processing is done.

This means: If you have just a single .dat file in your directory, it is sufficient to call the script without parameters:
 ```
> dat2txt.py
No jobname given.
Found  solve.dat
total force fx,fy,fz_NKW
>
 ```  

For example, the .dat-file might contain these lines:
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
Examples:
* [Drahtbiegen/Biegung/](../Drahtbiegen/Biegung/)
* [NonLinear/3PB/](../NonLinear/3PB/)

## monitor.py

This script reads the .sta and .cvg files for a given job and creates an image with two diagrams:

* force residuals, displacement correction and incremental time step ,
* step time and number of contact elements.

```
> monitor.py [<jobname>]
```
Specification of the jobname is only required if
there is more than one .sta file in the current directory.

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

### Usage

* Copy the file to be parametrized to `<filename>.par` or (better) `par.<filename>`, where `<filename>` can include any extension. This will become the source file for parametrization.

  Prefixing with `par.` is recommended, as this does not spoil the syntax highlighting in editors and you can call `param.py` without specifying the file name.

* In `<filename>.par` or `par.<filename>` add parameter definitions, preferrably in comment lines.   
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
If the filename starts with .par and only one such file is present in the directory, then it is sufficient to just call
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

### param.py vs. CGX valu

CGX supports parametrization starting with version 2.7 (see the `valu` command).

Advantages of param.py over CGX valu
* Works with older CGX versions
* Non-CGX-files can be parametrized (e.g. CCX input)
* More natural expressions (CGX has reversed polish notation)
* Large variety of available python functions

Disadvantages:
* Extra pre-processing step required
* Static replacement before use of the File (e.g. no access to the stack or to result values in postprocessing)

Examples:
* [Drahtbiegen/Zug/](../Drahtbiegen/Zug/)
* [Thermal/Thermal distortion/](../Thermal/Thermal distortion/)
* [Linear/StressConc1/](../Linear/StressConc1/)
* [NonLinear/3PB/](../NonLinear/3PB/)
