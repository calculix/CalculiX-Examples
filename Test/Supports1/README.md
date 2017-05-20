# Supports using distributing coupling
Tested with CGX/CCX 2.12

+ Use of distributing coupling to model bearings of a shaft
+ Modal analysis


File                           | Contents    
 :-------------                | :-------------
 [Welle.stp](Welle.stp)        | Geometry, STEP format, generated using Autodesk INVENTOR
 [pre.fbl](pre.fbl)            | CGX script, meshing with CGX
 [gmsh.fbl](gmsh.fbl)          | CGX script, meshing with Gmsh

The geometry represents a gearbox shaft with bearing journals at the ends. These are modelled using distributing coupling of the cylindrical bearing surfaces. The translations of their centroid is controlled by the displacement of the reference nodes.

Note that this works only for solid elements (not for shells).

The mesh is generated using Gmsh, as the meshing in CGX fails (massive production of elements with negative Jacobian, see issue #19).

<img src="Refs/mesh.png" width="400">

Constraints of the ref nodes

+ red: ux,uy,uz = 0
+ blue: uy, uz = 0


The shaft is free to rotate.

<img src="Refs/shape_1.gif" width="400">

Bending modes rotate about the centers of the bearing surfaces

<img src="Refs/shape_3.gif" width="400"><img src="Refs/shape_6.gif" width="400">

The left bearing is constrained in longitudinal direction (x), the right one is not. It is clearly visible that the bearing surfaces can deform (which they could not with kinematic coupling)

<img src="Refs/shape_12.gif" width="400">
