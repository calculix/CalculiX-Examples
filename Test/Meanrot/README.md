# Stress distribution with mean rotation MPC

Tested with CGX 2.19 / CCX 2.19

+ Test of mean rotation multipoint constraints
+ Stress distribution for applied moments
+ Result in version 2.13 and later: Exhibits the same strange (hyperbolic) stress distribution as distributing coupling in versions up to 2.18, plus stress peaks at boundaries and edges due to equal nodal weights. 
+ This example doesn't work in CGX 2.14.1 and 2.15.


File                           | Contents    
:-------------                | :-------------
[run.fbl](pre.fbl)            | CGX script, full simulation
[solve.inp](solve.inp)        | CCX input
[path.gpl](path.gpl)          | Gnuplot input for path plots
[test.py](test.py)            | Python script to run the full simulation

## Model description

The model consists of a thin rectangular plate. The bottom at z=0 is fixed (all dofs constrained).
To the upper surface, moments are applied via mean rotation MPC.

The meanrot MPC couples a set of nodes to a reference node:
 - The co-ordinates of the ref node specify the axis of rotation
 - Dof 1 of the ref node specifies the amount of rotation (in radians)

In CGX, you generate a `meanrot` MPC using the `send` command

    send load abq mpc df 1 0 0

with `load` being the coupled node set, `df` being the angle and `1 0 0` being the axis of rotation.
This generates input with the MPC definition including the definition of the reference node and with the constraint on the reference node.
The reference node number is the maximal node number + 1.

The reference node is not stored in the CGX node list, so you have to add a dummy node if you want to create another MPC. Store this node in a set for load application.

 
    seto refnode
    node ! 0 0 0
    setc refnode
  

For path plots of the stress distribution, appropriate node sets are generated.

## Simulation and Results

The plots of the normal stress show the load distribution for bending moments, the plots of the max shear stress show the load distribution in torsion.
```
> cgx -b run.fbl
```
<img src="Refs/mx.png" width="400"><img src="Refs/my.png" width="400">
<img src="Refs/mz-disp.png" width="400"><img src="Refs/mesh.png" width="400">

The stress profiles are hyperbolic with distance from the center of gravity (a linear distribution would be expected). The stress peaks at the corners and at the edge come from equal weight per node (in contrast to surface based distributing coupling, mean rot mpc is not area-aware).

<img src="Refs/stress.png">
