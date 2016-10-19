# Stress concentration in a flat strip with hole under bending load
Tested with CGX/CCX 2.11

+ Plane stress model
+ Parametric geometry and load
+ Load application via rigid body control nodes
+ Path and vector plots to show the stress distribution

File                           | Contents    
 :-------------                | :-------------
 [par.run.fbl](par.run.fbl)    | CGX script, complete analysis, parametrized with param.py
 [Stress.inp](Stress.inp)      | CCX input

To run the complete analysis, edit parameter values in [par.run.fbl](par.run.fbl)
and run
```
> param.py par.run.fbl
> cgx -b run.fbl
```

## Pre-Processing

The problem is parametrized using [param.py](../../Scripts/param.py). The geometry is built bottom-up by first defining points, then lines and then surfaces. The local mesh refinement at the stress concentration is controlled by division and growth rate of the individual lines.

In order to avoid restrictions to the line divisions, free meshing is used.

<img src="Refs/lines.png" width="400"><img src="Refs/mesh.png" width="400">

## Solving

The right edge nodes are coupled by a rigid body constraint. The displacement control node (ref node) is constrained in y and z, the rotation control node (rot node) in x and y. The bending moment is applied about z to the rotation control node. The moment is calibrated such that it creates a nominal bending stress of 1 MPa. Thus, the actual stress level in the solution can immediately be interpreted as stress concentration factor.

## Post-Processing

The stress state is evaluated using the worst principal stress (normal stress hypothesis with compression/tension symmetry). A vector plot shows the concentration in the symmetry plane. At the right edge, some deviations from the longitudinal direction can be seen. These are due to the suppression of y-strain at the rigid boundary. Leaving this aside, the rigid body constraint creates a much smoother load application than e.g. a pair of nodal forces at the vertices.

<img src="Refs/vecplot.png" width="400" title="Worst principal stress">
<img src="Refs/D.png"  width="400" title="Displacement, expanded geometry">

The stress concentration is illustrated by path plots.

The first one is defined based on a node set (all nodes at x=0), the second is defined based on a line set.
In a node set based definition, the points in the path plot directy correspond to mesh nodes. In a line based definition, new target nodes are created depending on the line division and the results are mapped from the source mesh to the target nodes.

<img src="Refs/nodepath.png"  title="Worst principal stress, path specified by node set">
<img src="Refs/linepath.png"  title="Worst principal stress, path specified by line set. There is a bug: target nodes without values (outside the structure) should interrupt the curve.">
