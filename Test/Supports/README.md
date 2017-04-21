# Supports using coupling
Tested with CGX/CCX 2.12

+ Test of distributing coupling
+ Modal analysis 

File                           | Contents    
 :-------------                | :-------------
 [pre.fbl](pre.fbl)            | CGX script, pre-processing
 [shapes.fbl](shapes.fbl)      | CGX script, post-processing, animation of mode shapes
 [solve.inp](solve.inp)        | CCX input

The model contains a brick shaped beam. The end at x=0 is controlled by a reference node via distributing coupling.

## Pre-Processing

The example demonstrates the automatic generation of a reference node at the cg of the surface in CGX. This is not essential for distributing coupling but will be for later tests with kinematic coupling.

```
> cgx -b pre.fbl
```

## Solving
The simulation consists of two frequency steps with different constraints of the reference node:
1. Free (no constraints)
2. Clamped (all dofs constrained)

For each step, 10 mode shapes are stored.
```
> ccx solve
```

## Post-Processing
```
> cgx -b shapes.fbl
```
Free (unconstrained reference node).

<img src="Refs/shape_1.gif" width="160"><img src="Refs/shape_2.gif" width="160"><img src="Refs/shape_3.gif" width="160"><img src="Refs/shape_4.gif" width="160"><img src="Refs/shape_5.gif" width="160">
<img src="Refs/shape_6.gif" width="160"><img src="Refs/shape_7.gif" width="160"><img src="Refs/shape_8.gif" width="160"><img src="Refs/shape_9.gif" width="160"><img src="Refs/shape_10.gif" width="160">

Clamped (all dofs of the ref node constrained). The constraints are in effect without preventing the end face from deforming.

<img src="Refs/shape_11.gif" width="160"><img src="Refs/shape_12.gif" width="160"><img src="Refs/shape_13.gif" width="160"><img src="Refs/shape_14.gif" width="160"><img src="Refs/shape_15.gif" width="160">
<img src="Refs/shape_16.gif" width="160"><img src="Refs/shape_17.gif" width="160"><img src="Refs/shape_18.gif" width="160"><img src="Refs/shape_19.gif" width="160"><img src="Refs/shape_20.gif" width="160">
