# Meshing a CAD Geometry

Tested with CGX 2.15 / CCX 2.15, Gmsh 4.4

This demonstrates possible workflows for a CalculiX analysis of a CAD
generated part.

* Starting point is a geometry created in Onshape and exported as STEP file.
* The FEA workflow is fully automated using CGX FBD files. There are two basic versions:
 * Meshing in gmsh (`run.fbd`)
 * Meshing in CGX (using cad2fbd for CAD file conversion)
   * `run1.fbd` demonstrates various mesh settings
   * `run2.fbd` performs a full analysis with the best settings found
* There are two versions for gmsh pre-processing:
  * `part.geo`: mesh the geometry as it is, leading to small elements at short edges and narrow surfaces
  * `partVT.geo`: Compounding lines and geometry before meshing.  

### Issues in Gmsh

+ virtual topology doesn't work
+ standard meshing requires very small elements to avoid  elements with negative jacobian



| File                     | Contents                                                       |
| :-------                 | :-------------                                                 |
| [part.step](part.step)   | STEP geometry exported from Onshape                            |
| [part.geo](part.geo)     | Gmsh control file for meshing and model display                |
| [run.fbd](run.fbd)       | CGX control file for preprocessing with gmsh,  solving and postprocessing |
| [run1.fbd](run1.fbd)     | CGX control file import with `cad2fbd` and meshing in CGX      |
| [run2.fbd](run2.fbd)     | CGX control file, import with `cad2fbd`, meshing, solving, postprocessing,    |
| [partVT.geo](partVT.geo) | Gmsh control file with geometry cleaning (virtual topology)    |
| [VTdemo.fbd](VTdemo.fbd) | CGX file for the mesh plots (original and VT version)          |
| [solve.inp](solve.inp)   | CCX input file                                                 |
| [test.py](test.py)       | python script to run the simulation                            |

# Run the analysis

The part is fixed on the rectangular base surface and a uniform pressure of 1 MPa
is applied to the top circular surface.

The complete analysis with gmsh-based meshing is run from a single CGX script. In order to proceed with
the analysis you have to close the gmsh window.
```
> cgx -b run.fbd
```
The individual steps of the workflow are discussed below.

Because the above script doesn't work with gmsh 4.4, an alternative gmsh-free control script is provided. It uses the CAD import tool `cad2fbd`.

```
> cgx -b run2.fbd
```


# Gmsh-Based Meshing

This is broken in Gmsh 4.4

The STEP geometry is loaded into gmsh and meshed with second order tetrahedra. Gmsh
also meshes the surfaces with individual sets of second order triangles.

Then, the physical groups have to be defined.
+ a phyiscal volume, named "part", containing the part
+ a physical surface "support", defining the area to be fixed
+ a physical surface "load", defining the area for pressure application

Upon export to ABAQUS format (inp) node and element sets for the physical groups are written.

The gmsh GEO file can be executed separately if you want to play around with the meshing details:
```
> gmsh part.geo
```
The result of the meshing is the file `gmsh.inp`

## Virtual Topology in Gmsh

The CAD model contains short edges and narrow faces, which locally enforce small elements.

Spurious edges and points can be removed by joining and re-parametrization of adjacent lines or surfaces using the commands
```
Compound Curve {old#1,old#2};
Compound Surface {old#1,old#2};

```
The Gmsh command file `partVT.geo` uses these commands to produce a mesh without spurious refinement spots.

This doesn't actually work in gmsh 4.4. The images below are generated with the maximum element size which still avoids negative jacobians.

Execute
```
> cgx -b VTdemo.fbd
```
to produce images for comparison of the meshes produced with the original geometry or with the cleaned geometry (virtual topology).

Original geometry (characteristic lenght 11, 4473 nodes, 2263 elements)

<img src="Refs/mesh.png" width="400" title="Mesh based on the original geometry"><img src="Refs/mesh1.png" width="400" title="Mesh based on the original geometry">

Virtual topology (characteristic length 5, 28149 nodes, 15635 elements):

<img src="Refs/VTmesh.png" width="400" title="Mesh based on the modified geometry, no local refinement spot any more"><img src="Refs/VTmesh1.png" width="400" title="Mesh based on the modified geometry, note the straight element edges on the arched surface.">

# Application of Boundary Conditions
After closing the gmsh window, CGX takes over control again and reads `gmsh.inp`.

You could do that interactively using
```
> cgx -c gmsh.inp
```
Then you might issue `prnt se` in order to see what sets are defined and `plot e` or `plot n` to
display individual sets (browse the sets by PageUp and PageDown).

Some cleanup is required, because gmsh writes 2D elements for the physical surfaces, which are not needed in CalculiX.

Remove the 2D elements (we address them by type here):
```
(cgx window) zap +CPS6
```
Extend node sets to face sets if required (here we need the set `load` for
pressure application)
```
(cgx window) comp load do
```
The following image shows the nodes of the support surface and the faces of the pressure
application surface.

<img src="Refs/sets.png" width="400" title="Sets for boundary application">

Once the sets are defined, there is no particular challenge any more with setting up the simulation.


# Results

von Mises stress, displaced geometry

<img src="Refs/disp.png" width="400" title="Displacement"><img src="Refs/se.png" width="400" title="von Mises stress">

# Meshing with cad2fbd/cgx

CGX comes with the CAD converter cad2fbd, which can convert STEP and IGES files to CGX native FBD format.

The script `run1.fbd`
+ calls the converter
+ reads the resulting file `result.fbd`
+ tries to mesh the geometry with various settings.
```
cgx -b run1.fbd
```
Unfortunately, CGX can't mesh all surfaces with moderate mesh density.

<img src="Refs/mesh_c2f.png" width="400" ><img src="Refs/mesh_c2f1.png" width="400">

If the mesh density is increased (all divisions multiplied by four) then automatic meshing succeeds (with nearly 150000 nodes, left image). If the high density is restricted to the lines along the narrow strips of the failed surface, then meshing succeeds with just 6000 nodes (right).

<img src="Refs/mesh_c2f2.png" width="400" ><img src="Refs/mesh_c2f3.png" width="400" >

# Gmsh-Free Analysis

Meshing is done in CGX as shown in the previous section.
The load and support surfaces are generated from the surface names in the imported geometry.
```
cgx -b run2.fbd
```
<img src="Refs/sets2.png" width="400" title="Sets for boundary application">

von Mises stress, displaced geometry

<img src="Refs/disp2.png" width="400" title="Displacement"><img src="Refs/se2.png" width="400" title="von Mises stress">
