# Properties of Cross Sections
Tested with CGX/CCX 2.10

+ Simply supported beam
+ Parametric section shapes of identical area
+ Symmetry reduction
+ Automatic extraction of results values

File                           | Contents    
 :-------------                | :-------------
 [par.pre.fbl](par.pre.fbl)    | CGX script, pre-processing, parametrized with param.py
 [post.fbl](post.fbl)          | CGX script, post-processing, images and bar chart
 [Biegung.inp](Test.inp)       | CCX input
 [barchart.gpl](barchart.gpl)  | Gnuplot file for the bar chart

The model contains several simply supported beams under gravity load of equal section area but different section shape.
Objective is to determine the relative stiffness and strength (yield limit) with respect to the square section.

<img src="Refs/mesh.png" width="400">

## Pre-Processing

The problem is parametrized using [param.py](../../Scripts/param.py). Starting from a given cross section area, the half span of the beam and a thickness, four section shapes of identical cross section area are generated.

The beams are supported vertically at all nodes at x=Length and have a symmetry boundary at x=0. One node per beam is fixed in y-direction.

The beams are loaded by their own weight, properies of steel are assumed.
```
> ../../Scripts/param.py par.pre.fbl
> cgx -b pre.fbl
```

## Solving
The simulation is essentially linear. The iterative procedure is used because of the presence of plastic material. Due to the low stresses, this does not affect the solution.
```
> ccx Biegung
```

## Post-Processing
```
> cgx -b post.fbl
```
The strength of a section shape is characterized by the section modulus, i.e. the ratio of applied bending moment divided by the maximum stress in the section. As all beams in the model carry the same load, they share the same bending moment.
The relative strength, therefore can be measured by the ratio of the inverse maximum stress values. As a reference, the square section is used (relative strength = 1).

The stiffness is the ratio of applied load to resulting deflection. Again, the relative stiffness is the deflection of a section divided by the value for the square section.

<img src="Refs/S11.png" width="400" title="Longitudinal stress. The higher the max. stress is, the lower is the strength of the beam for a given material">
<img src="Refs/D3.png"  width="400" title="Vertical displacement. Lower deflection means higher stiffness.">

The post-processing script extracts the maximum stress and deflection values for each section and generates a bar chart:

<img src="Refs/beams.png">
