# RVE with periodic boundary conditions
Tested with CGX 2.16 / CCX 2.15

This is a generic RVE of a fiber-matrix compound.

+ Brick-shaped unit cell
+ Structured mesh
+ Location-based assignment of material to elements
+ Periodic boundary conditions applied via helper script `periodic.py`

<img src="matrix-fiber.png" width="400">

Todo:
+ Output of the average nominal stress
+ Comfortable specification of load histories


File                   | Contents    
:-------------         | :-------------
[RVE.fbd](RVE.fbd)     | Pre-processing script for CGX (parametrized with valu commands)     
[post.fbd](post.fbd)   | Post-processing script for CGX (stress-strain curve and deformed plot)
[Solve.inp](Solve.inp) | CCX input
[test.py](test.py)     | Python script to run the full simulation

## Preprocessing

```
> cgx -b RVE.fbd
> periodic.py all.msh
```

The RVE represents a matrix material with unidirectional fibers arranged at a rectangular grid. Dimension  `lx` is irrelevant, as the material is uniform
in x direction. Dimensions `ly` and `lz` represent the fiber grid lengths.

The mesh consists of C3D8I elements and is controlled by a global node distance.

| Parameter | Value | Meaning |
| :------------- |  :------------- | :------------- |
| `lx` | 1 | length in x in mm |
| `ly` | 1 | length in y in mm |
| `lz` | 1 | length in z in mm |
| `rad` | 0.2 | fiber radius |
| `le` | 0.1 | node distance |

Constraints:

* `periodic.py` produces set definitions for control nodes and the equations for periodicity.
* Components of the average deformation gradient or of the average nominal stress (first Piola-Kirchhoff stress) can be specified as displacements or forces at the control nodes.
In the given example, the deformation gradient is a 20% stretch in x direction and a 20% shear on the y-plane in z direction. The components are prescribed as (x means unconstrained)
```
1 + 0.2    x       x
   0       x       0
   0      0.2      x
```
Given the edge length of 1, the above deformation gradient can be prescribed using
```
*boundary
nx,1,1,0.2
nx,2,3
ny,3,3,0.2
nz,2,2,0
```

<img src="matrix.png" width="400"><img src="fiber.png" width="400">

## Solving
```
> ccx Solve
```

## Postprocessing

Plots of the equivalent stress, the periodicity of the deformation is visible.
```
> cgx -b post.fbd
```


<img src="se.png" width="400" title="Equivalent stress"><img src="se-rot.png" width="400" title="Equivalent stress">
