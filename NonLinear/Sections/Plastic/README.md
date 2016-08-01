# Properties of Cross Sections (elasto-plastic)
Tested with CGX/CCX 2.10

+ Simply supported beam with a prescribed displacement in the center
+ Parametric section shapes of identical area
+ Symmetry reduction
+ Elasto-plastic material without hardening (ideal plastic)
+ Objective:
  + Evolution of the plastic zone
  + Force-displacement curves
  + Ultimate bending load - plastic section modulus (TBD)


File                           | Contents    
 :-------------                | :-------------
 [par.pre.fbl](par.pre.fbl)    | CGX script, pre-processing, parametrized with param.py
 [movie.fbl](movie.fbl)        | CGX script, movie generation
 [chart.fbl](chart.fbl)        | CGX script, chart generation
 [Biegung.inp](Biegung.inp)    | CCX input
 [df.gpl](df.gpl)              | Gnuplot script for the force-displacement-plot

## Pre-Processing

The problem is parametrized using [param.py](../../../Scripts/param.py).

The model contains several simply supported beams of equal section area but different section shape.

Objective is to visualize the evolution of the plastic zone and to determine the relative ultimate strength (full plastic section) with respect to the square section.

Starting from a given cross section area, the half span of the beam and a thickness, four section shapes of identical cross section area are generated.

The beams are supported vertically at all nodes at x=Length and z=0 and have a symmetry boundary at x=0.

One row of nodes per beam is fixed in y-direction. This is a bit over-constrained, but prevents lateral bending, which might happen due to the developing plastic hinges if just a single node per beam is constrained in y-direction.

The load is applied as a prescribed displacement of the nodes at x=0 (center between the supports) and at z=0 (through the section centroid).
```
> param.py par.pre.fbl
> cgx -b pre.fbl
```
<img src="mesh.png" width="400" title="Mesh density is biased towards the center section at x=0">
<img src="sets.png" width="400" title="">

## Solving
The ideal-plastic material can create convergence problems. These are mitigated by load application via prescribed displacement. A maximum increment size of 5% of the step is set for smooth force-displacement curves and movies.
```
> ccx Biegung
```
<img src="Biegung.png" >
## Post-Processing
```
> cgx -b movie.fbl
```
The plastic zone is marked using a two-step color scheme with the plastic proof strain of 0.2% marking the limit between the two colors. The right movie shows the longitudinal (bending) stress with color bar limits 5% above the yield limit.

<img src="PE.gif" width="400" title="Plastic zone (plastic strain &#60; 0.2% )">
<img src="SXX.gif" width="400" title="Bending stress">

To create a force-displacement-plot, type
```
> cgx -b -bg chart.fbl
```
Note that this script does not yet account for changes in the input file (maximum displacement is hard-wired).

<img src="df.png" title="Force-displacement-plot (full model)">
