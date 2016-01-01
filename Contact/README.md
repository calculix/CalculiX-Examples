# Shell Assembly
Tested with CGX/CCX 2.9 

+ Shell edge to shell face connection
+ Various contact versions
+ Modal analysis


| File                   | Contents                                      |
| :-------------         | :-------------                                |
| [pre.fbd](pre.fbd)     | Pre-processing script for CGX                 |
| [pc-ss.inp](pc-ss.inp) | CCX input, surface-to-surface penalty contact |
| [pc-ns.inp](pc-ns.inp) | CCX input, node-to-surface penalty contact    |
| [tie.inp](tie.inp)     | CCX input, MPC contact with `*tie`            |
| [equ.inp](equ.inp)     | CCX input, MPC contact with `*equation`       |

The only reliable contact version to connect face to edge of shell elements seems to be MPC contact with `*tie`.

## Preprocessing
Two separate parts are generated and meshed with shell elements.
```
cgx -b pre.fbd
```
<img src="model.png" width="300">

## Solving
Use the appropriate input file  for the contact version you want to test:
```
ccx tie
```

## Postprocessing

Load the results file in CGX
```
cgx tie.frd
```
Display animated mode shapes coloured with the displacement magnitude. Show the elements and increase the default scaling of the mode shapes.
```
view elem
scal d 2
ds 1 a 4
```
Browse through the individual mode shapes using the PageDown and PageUp keys.

<img src="mode9.png" width="300">
