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

<img src="sketch.png">

```
> param.py par.pre.fbd
> cgx -b pre.fbd
```
<img src="mesh.png"  width=400>

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
<img src="se.png" width="400" title="Equivalent stress">
<img src="se_exp.png" width="400" title="Equivalent stress, symmetry expansion of the model">

For wear prediction, contact pressure and slip are relevant.

<img src="path.png"  title="Contact pressure and slip">
