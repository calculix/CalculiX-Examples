# Thin-Walled Tube
Tested with CGX 2.10 / CCX 2.9

+ Modal and static analysis
+ Shell and solid model
+ Automatic movie generation in the post-processing
+ Application of distributed loads
+ Generation of a force-displacement curve

File                       | Contents    
 :-------------            | :-------------
 [values.fbd](values.fbd)  | CGX script, model parameters
 [geo.fbd](geo.fbd)        | CGX script, geometry plot
 [shell.fbd](shell.fbd)    | CGX script, pre-processing for the shell model    
 [solid.fbd](solid.fbd)    | CGX script, pre-processing for the solid model    
 [shell-modal.fbd](shell-modal.fbd)      |  CGX-script, complete  modal analysis of the shell model (including pre-post)
 [solid-modal.fbd](solid-modal.fbd)      |  CGX-script, complete  modal analysis of the solid model (including pre-post)
 [post-modal.fbd](post-modal.fbd)      |  CGX-script, Animation of mode shapes
 [post-solid-static.fbd](post-solid-static.fbd)      |  CGX-script, post-processing of the solid static simulation
[shell-modal.inp](shell-modal.inp)  | CCX input, modal analysis, shell model
  [solid-modal.inp](solid-modal.inp)  | CCX input, modal analysis, solid model
  [solid-static.inp](solid-static.inp)  | CCX input, static analysis, solid model
  [df.gpl](df.gpl)  | Gnuplot command file for the force-displacement-plot

## Shell Model, Modal Analysis

In order to avoid inconsistent use of the individual scripts, top level script files are provided, which contain the calls to pre-processing, solving and post-processing.
```
> cgx -b shell-modal.fbd
```
<img src="Refs/geo-shell.png" width="400" title="Shell model">
<img src="Refs/shell-modal-1.gif" width="400" title="Mode 1">


## Solid Model, Modal Analysis

```
> cgx -b solid-modal.fbd
```
<img src="Refs/geo-solid.png" width="400" title="Solid model">

The following animated gifs are created automatically in [post-modal.fbd](post-modal.fbd), wich is called by [solid-modal.fbd](solid-modal.fbd)

The movies contain one and a quarter cycles. This is because the gif movies are just played once on github and then remain static with the last frame displayed.

<img src="Refs/solid-modal-1.gif" width="400" title="Mode 1">
<img src="Refs/solid-modal-2.gif" width="400" title="Mode 2">
<img src="Refs/solid-modal-3.gif" width="400" title="Mode 3">
<img src="Refs/solid-modal-4.gif" width="400" title="Mode 4">

## Solid Model, Static Analysis

In the static analysis we apply a distributed load to the upper end of the tube. The generation of a force-displacement curve is demonstrated.

First, the mesh is generated:
```
> cgx -b solid.fbd
```
### Solution
The analysis consists of two steps.
 1. Full load is applied in negative x-direction, just the final results are written to the results files.
 2. The load is increased until it reaches the same value in positive x-direction. The results are written in small intervals for generation of a force-displacement curve
```
> ccx solid-static
> ../../Scripts/monitor.py solid-static
```
<img src="solid-static.png" width="600" title="Convergence plot">

### Postprocessing:
```
> cgx -b post-solid-static.fbd
```
Steps for generation of the  force-displacement curve:
 1. Extraction of the time history data from the dat-file using the script [dat2txt.py](../../Scripts/dat2txt.py).
 2. Creating a single file from the displacement history and the force history using the `join` shell command.
 3. Running Gnuplot with the command file [df.gpl](df.gpl).

The force-displacement plot is heavily non-linear because of the severe changes of the section moment of inertia due to ovalization.

 <img src="Refs/df-solid.png" title="Force-displacement plot">

 <img src="Refs/solid-SE-neg.png" width="400" title="Force applied in negative x-direction">
 <img src="Refs/solid-SE-pos.png" width="400" title="Force applied in positive x-direction">
