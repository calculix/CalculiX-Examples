# 90°-Bending of an Elastic Strip

This example demonstrates the application of prescribed rotations to node sets.
The structure is an elastic flat strip of dimensions 100x10x1 mm³. One end is
fixed and one end is rotated by 90°. The strip thus is bent into a quarter
circle. We investigate the following cases:

* Beam model
* Shell model
* Solid model with mean rotation constraint
* Solid model with rigid body constraint.

| File                        | Contents                                      |
| :-------------              | :-------------                                |
| [b.fbd](b-pre.fbd)          | CGX script, beam model                        |
| [b.inp](b.inp)              | CCX input, beam model                         |
| [sh.fbd](sh-pre.fbd)        | CGX script, shell model                       |
| [sh.inp](sh.inp)            | CCX input, shell model                        |
| [def-plot.fbd](def-plot.fbd)| CGX deformation plot                          |

# Beam Model
In CGX, b3 elements are specified. This results in B23R elements in the CCX input. These are internally expanded into C3D20R.

The rotation is applied as constraint to dof 5 of the node at the free end of the beam. With the default convergence control settings, only 12% of the specified rotation are reached.
```
> cgx -b b.fbd
```
The script contains the pre-processing, solution and post-processing.

<img src="b-mesh.png" width="300" title="Beam model">
<img src="b-def.png" width="300" title="Residual forces">

<img src="b.png" width="600" title="Convergence plot">

# Shell Model
In CGX, qu8 elements are specified. This results in S8R elements in the CCX input. These are internally expanded into C3D20R.

The rotation is applied as constraint to dof 5 of the nodes at the free end of the strip. The solution converges very well. Due to the large rotations, only invariant stress measures like v. Mises or principal stresses are useful.
```
> cgx -b sh.fbd
```

<img src="sh-mesh.png" width="300" title="Shell model">
<img src="sh-def.png" width="300" title="Residual forces">

<img src="sh.png" width="600" title="Convergence plot">

# Solid Model
