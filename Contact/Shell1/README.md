# Shell Assembly
Tested with CGX 2.10/CCX 2.9

+ Shell assembly with edge to face tied contact
+ Indenter with surface-to surface penalty contact

| File                   | Contents                                      |
| :-------------         | :-------------                                |
| [pre.fbd](pre.fbd)     | Pre-processing script for CGX                 |
| [post.fbd](post.fbd)   | Post-processing script for cgx                |
| [tie.inp](tie.inp)     | CCX input, MPC contact with `*tie`            |

## Preprocessing
A minimal sandwich structure is built with two skin sheets and a honeycomb core. #
The structure is supported at the edges of the bottom skin.
A roughly spherical indenter loads the upper skin.
```
> cgx -b pre.fbd
```
<img src="Refs/model.png" width="400">

## Solving
All nodes of the indenter are moved downwards in a static step with default solution controls.
```
> ccx tie
> ../../Scripts/monitor.py tie
```
<img src="tie.png" width="600">

## Postprocessing

Create a shaded image of the deformed structure
```
> cgx -b post.fbd
```

<img src="Refs/def.png" width="400">
