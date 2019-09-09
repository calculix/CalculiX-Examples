# Thin-Walled Tube
Tested with CGX 2.16 / CCX 2.15

+ Modal and static analysis
+ Shell and solid model
+ Full and half models (symmetry reduction)
+ Automatic movie generation in the post-processing
+ Application of distributed loads
+ Generation of a force-displacement curve


<img src="geometry.png" width="500" title="Geometry and parameters">


Model-independent files

File                       | Contents    
 :-------------            | :-------------
 [values.fbd](values.fbd)  | CGX script, model parameters
 [geo.fbd](geo.fbd)        | CGX script, geometry plot
 [post-modal.fbd](post-modal.fbd)      |  CGX-script, Animation of mode shapes
 [df.gpl](df.gpl)          | Gnuplot command file for the force-displacement-plot
 [test.py](test.py)        | Python script to run all simulations

In order to avoid inconsistent use of the individual scripts, top level script files are provided, which contain the calls to pre-processing, solving and post-processing.
## Reference for the mass properties
The theoretical mass and cg position are computed to compare with the values obtained by CGX for evaluation of geometric precision in CGX.

[![](Rohrknie-sm-screenshot.png)](http://smath.info/cloud/sheet/znPD3CdNqh)

Comparison for the paramters given in [values.fbd](values.fbd) and with C3D20R elements.

Model           | File    | Volume | x of cg    
 :------------  |:--      | --:    | --:  
 Reference    |     | 55860   | 41.59
 Solid full | [solid.fbd](solid.fbd)| 54881 | 41.15
 Solid full (45° sweep) | [solid1.fbd](solid1.fbd) | 55568| 41.48
 Solid half |  [solid-sym.fbd](solid-sym.fbd) | 27440 | 41.15

Model           | File    | Area | x of cg    
:------------  |:--      | --:    | --:  
Reference      |         | 56807  | 41.64
Shell full | [shell.fbd](shell.fbd)| 55965 | 41.30
Shell half |  [shell-sym.fbd](shell-sym.fbd) | 27982 | 41.30

Properties of the expanded elements

Model           | File    | Volume | x of cg    
 :------------  |:--      | --:    | --:  
 Reference      |         | 55860   | 41.59
 Shell full, expanded |  [shell-modal.fbd](shell-modal.fbd)| 55337 | 41.34
 Shell half |  [shell-sym-modal.fbd](shell-sym-modal.fbd) | 27709 | 41.37  


## Modal analysis results for solid/shell and full/reduced model

The mode frequencies for the first two symmetric mode shapes are compared. All models have the same mesh density and consist of a single layer of C3D20R elements (after shell expansion). For the shell models, the reference surface is the outside. This might lead to slightly increased mass.

Mode               | Solid full | Solid half | Shell full | Shell half|    
 :------------     | --:   | --:   | --:   | --:
 In-plane bending  | 337.2 | 337.2 | 339.9 | 350.5
 Ovalization       | 894.7 | 895.0 | 898.3 | 900.7

 <img src="Refs/solid-modal-1.gif" width="200" title="Solid full, Mode 1"> <img src="Refs/solid-sym-modal-1.gif" width="200" title="Solid reduced, Mode 1"> <img src="Refs/shell-modal-1.gif" width="200" title="Shell full, Mode 1"> <img src="Refs/shell-sym-modal-1.gif" width="200" title="Shell reduced, Mode 1">

 <img src="Refs/solid-modal-3.gif" width="200" title="Solid full, Mode 3"> <img src="Refs/solid-sym-modal-2.gif" width="200" title="Solid reduced, Mode 2"> <img src="Refs/shell-modal-3.gif" width="200" title="Shell full, Mode 3"> <img src="Refs/shell-sym-modal-2.gif" width="200" title="Shell reduced, Mode 2">

 The animated gifs are created automatically in [post-modal.fbd](post-modal.fbd), wich is called by the top level script for the individual models.


 The movies contain one and a quarter cycles. This is because the gif movies are just played once on github and then remain static with the last frame displayed.

## Full shell model, modal analysis

File                       | Contents    
 :-------------            | :-------------
 [shell.fbd](shell.fbd)    | CGX script, pre-processing for the shell model     
 [shell-modal.fbd](shell-modal.fbd)      |  CGX-script, complete  modal analysis of the shell model (including pre-post)
[shell-modal.inp](shell-modal.inp)  | CCX input, modal analysis, shell model

```
> cgx -b shell-modal.fbd
```
<img src="Refs/geo-shell.png" width="400" title="Full shell model">

<img src="Refs/shell-modal-1.gif" width="400" title="Mode 1"><img src="Refs/shell-modal-2.gif" width="400" title="Mode 2">
<img src="Refs/shell-modal-3.gif" width="400" title="Mode 3"><img src="Refs/shell-modal-4.gif" width="400" title="Mode 4">

## Half shell model, modal analysis

File                       | Contents    
 :-------------            | :-------------
  [shell-sym.fbd](shell-sym.fbd)    | CGX script, pre-processing for the shell model with symmetry     
 [shell-sym-modal.fbd](shell-sym-modal.fbd)      |  CGX-script, complete  modal analysis of the shell model with symmetry (including pre-post)
[shell-sym-modal.inp](shell-sym-modal.inp)  | CCX input, modal analysis, shell model with symmetry

```
> cgx -b shell-sym-modal.fbd
```
<img src="Refs/geo-shell-sym.png" width="400" title="Half shell model">

<img src="Refs/shell-sym-modal-1.gif" width="400" title="Mode 1"><img src="Refs/shell-sym-modal-2.gif" width="400" title="Mode 2">
<img src="Refs/shell-sym-modal-3.gif" width="400" title="Mode 3"><img src="Refs/shell-sym-modal-4.gif" width="400" title="Mode 4">

## Full Solid model

File                       | Contents    
 :-------------            | :-------------
 [solid.fbd](solid.fbd)    | CGX script, pre-processing for the solid model    
  [solid-modal.fbd](solid-modal.fbd)      |  CGX-script, complete  modal analysis of the solid model (including pre-post)
 [post-solid-static.fbd](post-solid-static.fbd)      |  CGX-script, post-processing of the solid static simulation
  [solid-modal.inp](solid-modal.inp)  | CCX input, modal analysis, solid model
  [solid-static.inp](solid-static.inp)  | CCX input, static analysis, solid model

### Full solid model, modal analysis

```
> cgx -b solid-modal.fbd
```
<img src="Refs/geo-solid.png" width="400" title="Full solid model">

<img src="Refs/solid-modal-1.gif" width="400" title="Mode 1"><img src="Refs/solid-modal-2.gif" width="400" title="Mode 2">
<img src="Refs/solid-modal-3.gif" width="400" title="Mode 3"><img src="Refs/solid-modal-4.gif" width="400" title="Mode 4">



### Full solid model, static analysis

In the static analysis we apply a distributed load to the upper end of the tube, without constraining the cross section shape using the `*distributing coupling` command.
The nodes of the lower left end are completely constrained.

The generation of a force-displacement curve is demonstrated.

First, the mesh is generated:
```
> cgx -b solid.fbd
```

#### Solution
The analysis consists of two steps.
 1. Full load is applied in negative x-direction, just the final results are written to the results files.
 2. The load is increased until it reaches the same value in positive x-direction. The results are written in small intervals for generation of a force-displacement curve
```
> ccx solid-static
> monitor.py solid-static
```
<img src="solid-static.png" width="600" title="Convergence plot">

#### Postprocessing:
```
> cgx -b post-solid-static.fbd
```
Steps for generation of the  force-displacement curve:
 1. Extraction of the time history data from the dat-file using the script [dat2txt.py](../../Scripts/dat2txt.py).
 2. Creating a single file from the displacement history and the force history using the `join` shell command.
 3. Running Gnuplot with the command file [df.gpl](df.gpl).

The force-displacement plot is heavily non-linear because of the severe changes of the section moment of inertia due to ovalization. The displacement range for which convergence of the solver can be obtained depends on the element type and the mesh density. Here we use C3D20R elements.

 <img src="Refs/df-solid.png" title="Force-displacement plot">

 <img src="Refs/solid-SE-neg.png" width="400" title="Force applied in negative x-direction"><img src="Refs/solid-SE-pos.png" width="400" title="Force applied in positive x-direction">

## Half solid model, modal analysis

 File                       | Contents    
  :-------------            | :-------------
  [solid-sym.fbd](solid-sym.fbd)    | CGX script, pre-processing for the solid model    
   [solid-sym-modal.fbd](solid-sym-modal.fbd)      |  CGX-script, complete  modal analysis of the solid model (including pre-post)
   [solid-sym-modal.inp](solid-modal.inp)  | CCX input, modal analysis, solid model

 ```
 > cgx -b solid-sym-modal.fbd
 ```
 <img src="Refs/geo-solid-sym.png" width="400" title="Half solid model">

 <img src="Refs/solid-sym-modal-1.gif" width="400" title="Mode 1"> <img src="Refs/solid-sym-modal-2.gif" width="400" title="Mode 2">
 <img src="Refs/solid-sym-modal-3.gif" width="400" title="Mode 3"> <img src="Refs/solid-sym-modal-4.gif" width="400" title="Mode 4">
