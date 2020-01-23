# 90°-Bending of an Elastic Strip
Tested with CGX 2.16 / CCX 2.15

This example demonstrates the application of prescribed rotations to node sets.
The structure is an elastic flat strip of dimensions 100x10x1 mm³. One end is
fixed and one end is rotated by 90°. The strip thus is bent into a quarter
circle. We investigate the following cases:

* Beam model
* Shell model
* Solid model with mean rotation constraint,
* Solid model with rigid body constraint,
* Solid model with coupling/distributing constraint,
* Solid model with coupling/kinematic constraint,



Model                    | CGX input        | CCX input
:-------                 | :-------------   |:---        
Beam                     | [b.fbd](b.fbd)   | [b.inp](b.inp)
Shell                    | [sh.fbd](sh.fbd) | [sh.inp](sh.inp)
Solid, mean rotation MPC | [sm.fbd](sm.fbd) | [sm.inp](sm.inp)
Solid, rigid body MPC    | [sr.fbd](sr.fbd) | [sr.inp](sr.inp)
Solid, Coupl./Distrib.   | [scd.fbd](scd.fbd) | [scd.inp](scd.inp)
Solid, Coupl./Kinem.     | [sck.fbd](sck.fbd) | [sck.inp](sck.inp)



Other files         | Contents     
:-------------              | :-------------
[def-plot.fbd](def-plot.fbd)| CGX input for deformation plot
[view.fbd](view.fbd)        | CGX input for view settings   
[test.py](test.py)| Python script to run all simulations

## Reference solution
Click the image below to open a life SMath worksheet

[![Streifen](Streifen.png)](http://en.smath.info/cloud/worksheet/Wd6n8P2K)


# Beam Model
In CGX, be3r elements are specified. This results in B32R elements in the CCX input. These are internally expanded into C3D20R.

The rotation is applied as constraint to dof 5 of the node at the free end of the beam. With the default convergence control settings, only 6% of the specified rotation are reached.
```
> cgx -b b.fbd
```
The script contains the pre-processing, solution and post-processing.

<img src="b-mesh.png" width="300" title="Beam model"><img src="b-def.png" width="300" title="Residual forces">

<img src="b.png" width="600" title="Convergence plot">

# Shell Model
In CGX, qu8r elements are specified. This results in S8R elements in the CCX input. These are internally expanded into C3D20R.

The rotation is applied as constraint to dof 5 of the nodes at the free end of the strip. The solution converges very well. Due to the large rotations, only invariant stress measures like v. Mises or principal stresses are useful.
```
> cgx -b sh.fbd
```

<img src="sh-mesh.png" width="300" title="Shell model"><img src="sh-def.png" width="300" title="Worst principal stress">

<img src="sh.png" width="600" title="Convergence plot">

# Solid Model
In CGX, he20r elements are specified. This results in C3D20R elements in the CCX input.

## Mean Rotation MPC
The rotation is applied using the mean rotation multipoint constraint (MPC). This couples the mean rotation of a cloud of nodes to the first dof of a reference node. The initial position of that node indicates the axis of rotation.

In CGX, the required input for a rotation of 90° about the y-axis can be generated using the command
```
send rot abq mpc 90 0 1 0
```
This generates the files
* [rot.mpc](rot.mpc) with the ref node definition and the `*mpc` block (model data)
* [rot.bou](rot.bou) with the `*boundary` block (step data)

Run the analysis:
```
> cgx -b sm.fbd
```
At 28% of the specified deformation, the incremental time becomes too small and the solution is stopped.

<img src="sm-mesh.png" width="300" title="Solid model with mean rotation MPC"><img src="sm-def.png" width="300" title="Residual forces">

<img src="sm.png" width="600" title="Convergence plot">

## Rigid Body Constraint
The rotation is applied using a rigid body constraint. The right end is rigidly coupled to a rotation control node. In the pre-processing, it is useful to create the control node with a fixed number before meshing.

Run the analysis:
```
> cgx -b sr.fbd
```
At 74% of the specified deformation, the incremental time becomes too small and the solution is stopped.

<img src="sr-mesh.png" width="300" title="Solid model with rigid body MPC"><img src="sr-def.png" width="300" title="Residual forces">

<img src="sr.png" width="600" title="Convergence plot">

## Coupling/Distributing
The rotation is applied using surface based distributed coupling
```
*coupling,refnode=1,surface=Srot,constraint name=rot
*distributing
5
```
and
```
*boundary
Nrefnode,5,5,1.57
```

Run the analysis:
```
> cgx -b scd.fbd
```
The simulation runs but the free end exhibits some hourglassing-like distortion.

<img src="scd-mesh.png" width="300" title="Solid model with surfaced based load (distributing coupling)"><img src="scd-def.png" width="300" title="Residual forces">

<img src="scd.png" width="600" title="Convergence plot">

## Coupling/Kinematic
The rotation is applied using surface based kinematic coupling (with the y-displacement not coupled)
```
*coupling,refnode=1,surface=Srot,constraint name=rot
*kinematic
1
3
```
and
```
*boundary
Nrefnode,5,5,1.57
Nrefnode,2,2
```

Run the analysis:
```
> cgx -b sck.fbd
```
At 78% of the specified deformation, the incremental time becomes too small and the solution is stopped.

<img src="sck-mesh.png" width="300" title="Solid model with surface based load (kinematic coupling)"><img src="sck-def.png" width="300" title="Residual forces">

<img src="sck.png" width="600" title="Convergence plot">
