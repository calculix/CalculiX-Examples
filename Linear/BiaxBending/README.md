# Unsymmetric Bending
Tested with CGX/CCX 2.12

+ Application of bending moment via kinematic coupling without transverse constraints
+ Display of the neutral fiber

File                           | Contents    
 :-------------                | :-------------
 [par.run.fbl](par.run.fbl)    | CGX script top level script, parametrized with param.py
 [Biegung.inp](Biegung.inp)    | CCX input

## Model

The model contains a cantilever beam with bending moment about the transverse horizontal axis (y). It is applied to the ref node of a kinematic coupling constraint o the free end surface. The cross section is a rectangle rotated by 45°.

<img src="Refs/mesh.png" width="400">

In order to not induce transverse stresses by the coupling constraint, the constraint is restricted to dof 1 (longitudinal direction) of the surface nodes.
```
*coupling, ref node=1, surface=Sload, constraint name=c1
*kinematic
1
```
This only couples the x displacement and the rotation about y and z of the reference node to the surface. Thus, dofs 2,3 and 4 of the ref node have to be constrained separately.

## Results

```
> param.py par.run.fbl
> cgx -b run.fbl
```
<img src="Refs/sxx.png"  width="400" title="Longitudinal stress."><img src="Refs/neutral.png"  width="400" title="Neutral fiber">
