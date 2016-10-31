# Engine Valve
Tested with CGX/CCX 2.11

+ Axisymmetric model of a valve with valve seat
+ Linear elastic material
+ Penalty contact with friction
+ Path plot of contact pressure and slip
+ Pressure load



| File                   | Contents                                      |
| :-------------         | :-------------                                |
| [par.pre.fbd](par.pre.fbd)     | Pre-processing script for CGX  (parametrized with `param.py`)                |
| [valve.inp](valve.inp) | CCX input |
| [post.fbd](post.fbd)   | CGX post-processing script                    |
| [path.gnu](df.gnu)   | Gnuplot script for the contact plot    |

## Preprocessing
The valve and the valve seat ring are meshed with axisymmetric second order triangular elements. This allows for free meshing,

The mesh is controlled by a global size and the division on the contact region of the valve (dependent side, orange).

<img src="sketch.pdf">

```
> param.py par.pre.fbd
> cgx -b pre.fbd
```
<img src="mesh.png">

## Solving
```
> ccx valve
> monitor.py valve
```
<img src="valve.png" title="Convergence plot">

## Postprocess

```
> cgx -b post.fbd
```
<img src="SE.png" width="400" title="Equivalent stress">
<img src="PE.png" width="400" title="Equivalent plastic strain">

The force-displacement curve is valid for the half model and is created from the .dat-file-output
of the total reaction forces and the displacement of the monitor node.

<img src="df.png" width="400" title="Force-displacement curve">

Stress profiles in cross sections at the support (left) and at the eye (right, light blue in the mesh plot). The diagrams show the profiles at the first increment (still elastic) and at the end of the load step.

<img src="SXX-fix.png" width="400" title="Stress profile at the support">
<img src="SXX-path.png" width="400" title="Stress profile at x=0">
