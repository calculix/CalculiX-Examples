# Tensile Test
Tested with CGX 2.10/CCX 2.10

Tensile test of a wire of 1 mm diameter made of 1.4301 stainless steel. This steel has a high yield strength but nearly no work hardening, thus the uniform strain is very low and necking occures early and very localized.

<img src="movie.gif" width="300" title="plastic equivalent strain">
<img src="2D3D.png" width="300" title="3D expansion with embedded 2D model">

The model is axisymmetric and represents a 2 mm piece of the wire with full displacement constraint at one end and symmetry at the other end. Necking occures in the symmetry plane.

+ Large displacements
+ Plasticity
+ Parametrization alternatives (param.py or CGX valu)

| File     | Contents    |
| :------------- | :------------- |
| [vpre.fbd](vpre.fbd)     | Pre-processing script for CGX (parametrized with valu commands)     |
| [pre.fbd.par](pre.fbd.par)     | Pre-processing script for CGX (parametrized with param.py)  |
| [plots.fbd](plots.fbd) | Post-processing script for CGX (history and path plots) |
| [expansion.fbd](expansion.fbd) | Post-processing script for CGX (axisymmetric expansion) |
| [2D.fbd](2D.fbd) | Post-processing script for CGX (2D display) |
| [Zug.inp](Zug.inp) | CCX input |

## Preprocessing
This example is designed with two alternative ways for parametrization. Both produce equivalent results.

The mesh is biased as to account for the localized deformation.

<img src="zug-geo.png" width="400">

Boundary conditions:
* uy = 0 at y = 0 (symmetry boundary)
* uy = 2 at y = 0.3 (displacement controlled extension at the upper edge)
* ux = 0 at x = 0 (restrict nodes to the symmetry axis)

#### Parametrization with param.py
See [../../Scripts/](../../Scripts/) for details
```
> ../../Scripts/param.py pre.fbd.par
> cgx -b pre.fbd
```
#### Parametrization with CGX valu
```
> cgx -b vpre.fbd
```
## Solving
```
> ccx Zug
> ../../Scripts/monitor.py Zug
```
The second command generates a convergence history plot of the solution.
<img src="Zug.png" title="Convergence history">

## Postprocessing
#### Path plot
```
> cgx -b plots.fbd
```
This creates path plots of the plastic equivalent strain along the symmetry axis (ine `l1` from point `cp` to point `c0`) and then in radial direction (line `l2` from point `c0` to point `rad`).

The first plot is based on the **undeformed** geometry:

<img src="path0geo.png" width="300" title="Path on the undeformed model">
<img src="path0.png" width="500" title="Path plot of the equivalent strain">

The second plot is based on the **deformed** geometry:

<img src="pathgeo.png" width="300" title="Path on the deformed model">
<img src="path.png" width="500" title="Path plot of the equivalent strain">

#### Symmetry expansion
Beginning with version 2.10, CGX can sweep 2D elements with results attached. This is used for symmetry expansion of the axisymmetric 2D output.
```
> cgx -b expansion.fbd
```
<img src="PE-expanded.png" width="300" title="Automatically generated plot of the plastic equivalent strain with symmetry expansion">
<img src="expanded.png" width="300" title="This image is darker than expected.">
<img src="2D3D.png" width="300" title="3D expansion with embedded 2D model">

To see just the non-expanded model, use this command:
```
> cgx -b 2D.fbd
```
<img src="PE-2D.png" width="300" title="same plot as above without symmetry expansion">
