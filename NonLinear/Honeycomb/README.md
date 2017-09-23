# Honeycomb Sandwich
Tested with CGX 2.12.1/CCX 2.12

There are issues with the convergence control.

+ Non-linear static analysis
+ Plasticity
+ Penalty contact
+ Symmetry reduction
+ Parametric model
+ Shell elements

File                        | Contents    
:-------------              | :-------------
[par.pre.fbl](par.pre.fbl)  | CGX script, pre-processing, parametrized with `param.py`
[pre.fbl](pre.fbl)          | CGX script, pre-processing, already processed with `param.py`
[post.fbd](post.fbd)        | CGX script, post-processing
[Biegung.inp](Biegung.inp)  | CCX input
[df.gnu](df.gnu)            | Gnuplot script


The model represents a four point bending test on an elasto-plastic aluminium honeycomb sandwich plate. The honeycombs are of expanded type, i.e. 1/3 of the walls has double thickness.

Parameter | Description
:---      | :-----
`le`      | Length of double-thickness walls
`wb`      | Cell width in expansion direction
`hw`      | Heigth of the core
`lx`      | Half sample target length
`ly`      | Half sample target width
`x1`      | Distance from center to upper cylinder (indenter)
`x2`      | Distance from center to lower cylinder (support)
`radius`  | Radius of the cylinders
`tupper`  | Thickness of the upper face sheet
`tlower`  | Thickness of the lower face sheet
`tsingle` | Thickness of the core material
`divx`    | Division of the (half) walls in x direction
`divy`    | Division of the angled walls in y direction
`divz`    | Division of the walls in z direction

## Pre-Processing

You may edit the file [par.pre.fbl](par.pre.fbl) and then run
```
> param.py par.pre.fbl
> cgx -b pre.fbl
```
First, a unit cell is generated and then copied in x- and y-direction as many
times as is required to fit the target dimensions.

Then, all elements off the target are are cut away.

<img src="size.png" width="400" title="Sample cut out of the generated material"><img src="core.png" width="400" title="Cell walls: single thickness (light blue), double thickness (dark blue)">

The cylinders for load application and support are completely displacement controlled, they have
no degrees of freedom.

<img src="quarter.png" width="400" title="Quarter sample with load application and support cylinders">

Shell elements expanded to a single layer of volume elements are not really appropriate for plastic deformations, because they have just two cross thickness integration points.

## Solving
The rate of convergence is affected by the plastic material, the mesh density, the contact stiffness and the time incrementation controls.
```
> ccx Biegung
> monitor.py Biegung
```
<img src="Biegung.png" title="Convergence plot">

## Post-Processing
```
> cgx -b post.fbd
```
<img src="df.png" title="Force-displacement curve (for the full specimen)">

<img src="PE.png" width="400" title="Equivalent strain"><img src="PE-core.png" width="400" title="Equivalent strain in the core"><img src="SE.png" width="400" title="Equivalent stress"><img src="SE-core.png" width="400" title="Equivalent stress in the core">
