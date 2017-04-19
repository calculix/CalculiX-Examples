# Shell Assembly
Tested with CGX/CCX 2.12

+ Shell assembly with edge to face tied Lagrange contact
+ Indenter with surface-to surface penalty contact
+ Indenter generated with nurbs based sweep, this generates a more precise hemisphere

| File                   | Contents                                      |
| :-------------         | :-------------                                |
| [pre.fbd](pre.fbd)     | Pre-processing script for CGX                 |
| [post.fbd](post.fbd)   | Post-processing script for cgx                |
| [tie.inp](tie.inp)     | CCX input, MPC contact with `*tie`            |

## Preprocessing
A minimal sandwich structure is built with two skin sheets and a honeycomb core.
The structure is supported at the edges of the bottom skin.
The spherical indenter loads the upper skin.
```
> cgx -b pre.fbd
```
<img src="Refs/model.png" width="400">

## Solving
All nodes of the indenter are moved downwards in a static step with default solution controls.
```
> ccx tie
> monitor.py tie
```
<img src="tie.png" width="600">

## Postprocessing

Create a shaded image of the deformed structure
```
> cgx -b post.fbd
```

<img src="Refs/def1.png" width="400" title="Deformed geometry"><img src="Refs/worstPS1.png" width="400" title="Worst principal stress">
