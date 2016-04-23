# Stress Concentration
Tested with CGX 2.10 / CCX 2.9

+ Axisymmetric part under tensile load
+ Stress gradient

File                           | Contents    
 :-------------                | :-------------
 [par.pre.fbl](par.pre.fbl)    | CGX script, pre-processing, parametrized with param.py
 [post.fbl](post.fbl)          | CGX script, post-processing,
 [Stress.inp](Stress.inp)      | CCX input

## Pre-Processing

```
> ../../Scripts/param.py par.pre.fbl
> cgx -b pre.fbl
```

The problem is parametrized using [param.py](../../Scripts/param.py). The geometry is built bottom-up by first defining points, then lines and then surfaces. The local mesh refinement at the stress concentration is controlled by division and bias of the individual lines.

In order to avoid restrictions to the line divisions, free meshing is used.

The left end at y=0 is fixed in axial direction, at the right end, a uniform tensile stress of 100 (in units of force divided by area) is applied.

<img src="Refs/div.png" width="400"><img src="Refs/mesh.png" width="400">


## Solving
```
> ccx Stress
```

## Post-Processing
```
> cgx -b post.fbl
```
The stress concentration factor is the maximum stress divided by the applied nominal stress (100 MPa).

<img src="Refs/worstps.png" width="400" title="Worst principal stress">
<img src="Refs/worstps-zoom.png"  width="400" title="Worst principal stress">
