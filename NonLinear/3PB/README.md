# Three-point bending test of a hollow profile
Tested with CGX/CCX 2.10

+ Non-linear static analysis
+ Plasticity
+ Penalty contact
+ Symmetry reduction

File                       | Contents    
 :-------------            | :-------------
 [par.pre.fbl](par.pre.fbl)        | CGX script, pre-processing, parametrized with `param.py`
 [post.fbl](post.fbl)      | CGX script, post-processing, plots and force-displacement curve
 [cpost.fbl](cpost.fbl)      | CGX script, post-processing, movie
 [Biegung.inp](Biegung.inp) | CCX input
 [df.gpl](df.gpl) | Gnuplot control file for the force-displacement plot

The model represents a three point bending test on a elasto-plastic beam with a hollow box section. The simulation
domain is reduced to a quarter due to symmetry.

## Pre-Processing

You may adjust the parameter values in the file [par.pre.fbl](par.pre.fbl) and then run
```
> param.py par.pre.fbl
> cgx -b pre.fbl
```
<img src="Refs/parts.png" width="400" title="Parts: Specimen, indenter and support">

<img src="Refs/groups.png" width="400" title="Node groups for constraint application">
<img src="Refs/pairs.png" width="400" title="Contact pairs">

The load application cylinders are controlled by imposed displacements to the nodes in the y=0 plane.

## Solving
The time step has to be limited for stable contact. Initially, the number of contact
elements grows with increasing indentation, but then shrinks due to local buckling below the indenter.
```
> ccx Biegung
> monitor.py Biegung
```
<img src="Biegung.png" title="Convergence plot">

## Post-Processing
A movie showing the contact details:
```
> cgx -b cpost.fbl
```
<img src="movie.gif"  title="contact zone">

```
> cgx -b post.fbl
```
The plastic strain is displayed, the color bar is restricted to 0...4%.

<img src="Refs/PE.png"  title="Equivalent strain">
<img src="Refs/PEexpanded.png"  title="Equivalent strain, expanded model">

<img src="Refs/PEexpanded_y.png" width="400"  title="Equivalent strain, expanded model"><img src="Refs/PEexpanded_yx.png" width="400"  title="Equivalent strain, expanded model">

A force-displacement-curve is generated:
<img src="Refs/df.png" title="Force-Displacement Curve">
