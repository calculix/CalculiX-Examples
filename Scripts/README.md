# Helper Scripts
These script augment the automation capabilities of CGX.

File                    | Contents    
 :-------------         | :-------------
 [dat2txt.py](dat2txt.py)     | Extract time history data from .dat files     
 [monitor.py](monitor.py)   | Create convergence plots based on the .cvg and .sta files
 [param.py](param.py) | Preprocessor tor python expressions in arbitrary files

## dat2txt.py

 This script extracts arbitrary result items from a given .dat file to an easy to parse tabular text file with one line per time point.
 ```
 python dat2txt,py <jobname>
 ```  
This reads `<jobname>.dat` and writes a text file for each result item in the .dat file.

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
* [Drahtbiegen/Biegung/](Drahtbiegen/Biegung/)

## monitor.py

This script reads the .sta and .cvg files for a given job and creates a plot of the force residuals, the displacement correction and the incremental time step in the upper diagram and of the total step time in the lower diagram.
```
python monitor.py <jobname>
```
The plot is displayed and written to `<jobname>.png`.

Examples:
* [Drahtbiegen/Biegung/](Drahtbiegen/Biegung/)
* [Pillow/](Pillow/)
* [Kasten/](Kasten/)

## param.py

This script allows you to parametrize text files. Parametrization means that
you replace literal values (strings or numeric values) in text files by
expressions. These expressions can contain variables, which can be defined at
the beginning (or elsewhere in the file) and can be referenced wherever below
their definition.

### Usage

* Copy the file to be parametrized to `<filename>.par`, where `<filename>` can include any extension. This will become the source file for parametrization.

* In `<filename>.par` add parameter definitions, preferrably in comment lines.   
  * To assign the value 4 to the variable a, include `<a=4>` to such a line.
  * To reference the value just add `<a>` wherever the value has to go.
  * Wherever you need a value depending on a, write something like `<b=a^2>` or
   `<-a>`. If you want floating point results, make sure to use floating point
   variables or values (with a period. eg. `<a=2.>`).

* To extract a usable file `<filename>`, run
```
python param.py <filename>.par
```
The expressions are scanned and the angle brackets
replaced (pre-processing):
  * Variable definitions are copied verbatim to the output (for reference/documentation).   
  * Expressions are replaced by their result.


|                 | `<filename>.par` |`<filename>` |
|  :------------- | :-------------   |:--          |
|  Definitions    | `<a=2>`          |`a=2`        |
|                 | `<b=2*a>`        |`b=2*a`      |
|                 | `<type="he8">`   | `type=”he8”`|
|  Expression     | `<a>`            | `2`         |
|                 | `<2*a>`          | `4`         |
|                 | `<b>`            | `4`         |
|                 | `<a+b>`          | `6`         |
|                 | `<type>`         | `he8`       |

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
