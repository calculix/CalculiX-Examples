# CalculiX-Examples
Created by Martin Kraska, Brandenburg University of Applied Sciences

These examples demonstrate the use of [CalculiX](http://www.dhondt.de/) for various analysis types.
Also, there are some helper python scripts.

All examples are developed and tested with CalculiX 2.10 in the virtual box provided by Sven Kaßbohm at [fiziko.de](http://www.fiziko.de/vbox/). It is configured such that you can easily compile new versions of CCX and CCX. It has, however, some disadvantages:

* Hardware Open GL does not work
* Multithreading does not work.

These are not relevant for simple educational models but are definitely relevant for serious work.

For editing CGX, CCX  or gmsh input under linux, I recommend [atom](https://atom.io/), it has syntax highlighting for these files and markdown preview. The README-files for the examples here are written in Markdown.

Under Windows, I recommend the [bConverged](http://bconverged.com/) build. It has nice SciTE integration with syntax highlighting. Some examples may require adjustments of the system calls (like echo, mv and other commands)

[<img
  src="Drahtbiegen/Biegung/movie.gif"
  width="200"
  title="Bending of a wire. Large deformations, plasticity, rigid body control">
](Drahtbiegen/Biegung/)
[<img
  src="Kasten/hcpy_2.png"
  width="200"
  title="Compression of a box. Non-linear buckling, structure, internal pressure as imperfection">
](Kasten/)
[<img
  src="Elements/Solid/solid_C3D4_20_S.png"
  width="200"
  title="Convergence study for solid elements in linear elasticity">
](Elements/Solid/)
[<img
  src="Contact/mode9.png"
  width="200"
  title="Shell edge to shell face connection, modal analysis">
](Contact/)
[<img
  src="Pillow/expanded2.png"
  width="200"
  title="Inflation of a square pillow. Non-linear static analysis, symmetry expansion in post-processing">
](Pillow/)
[<img
  src="Drahtbiegen/Zug/movie.gif"
  width="200"
  title="Tensile test, axisymmetric model, expanded in postprocessing, path plot demo">
](Drahtbiegen/Zug/)
[<img
  src="Streifen/sh-def.png"
  width="200"
  title="Bending of an elastic strip, beam, shell and solid models with various rotation constraints">
](Streifen/)
[<img
  src="Thermal/Thermal distortion/SE-pcss-exp.png"
  width="200"
  title="Welded T-joint, assembly with different contact formulations, shrinkage model for the distortion">
](Thermal/Thermal distortion/)
[<img
  src="Contact/Hertz_2D/SE.png"
  width="200"
  title="Hertz contact stress, plane strain, linear elasticity">
](Contact/Hertz_2D/)
[<img
  src="Linear/Plates/2D3D.png"
  width="200"
  title="Clamped circular plates, axisymmetric model">
](Linear/Plates/)
[<img
  src="NonLinear/Rohrknie/Refs/solid-SE-neg.png"
  width="200"
  title="Thin-walled tube, static and modal analysis">
](NonLinear/Rohrknie/)
[<img
  src="Thermal/Thermografie/movie.gif"
  width="200"
  title="Thermografic testing of an overlap weld, transient thermal analysis">
](Thermal/Thermografie/)
[<img
  src="NonLinear/Sandwichtest/Refs/PE-expanded.png"
  width="200"
  title="4-point bending test of a sandwich structure">
](NonLinear/Sandwichtest/)
[<img
  src="NonLinear/Sections/Refs/D3.png"
  width="200"
  title="Different section shapes of identical area. Automatic determination of relative strength and stiffness">
](NonLinear/Sections/)
[<img
  src="Linear/StressConc/Refs/worstps.png"
  width="200"
  title="Stress concentration factor">
](Linear/StressConc/)
[<img
  src="Linear/StressConc1/Refs/D.png"
  width="200"
  title="Stress concentration factor, flat strip with hole, bending load, vector and path plots">
](Linear/StressConc1)
[<img
  src="Contact/Shell1/Refs/def.png"
  width="200"
  title="Shell assembly, rigid intenter, penalty contact">
](Contact/Shell1/)
[<img
  src="CAD/OnshapeTutorial/Refs/se.png"
  width="200"
  title="CAD part, meshed in gmsh">
](CAD/OnshapeTutorial/)
[<img
  src="Linear/Crack1/Refs/se.png"
  width="200"
  title="CT specimen, determination of the energy release rate">
](Linear/Crack1/)
[<img
  src="Contact/Leafspring/Refs/Sxx.png"
  width="200"
  title="Parametric model of a leaf spring. Penalty contact">
](Contact/Leafspring/)
[<img
  src="Linear/ShearCenter/Refs/Sxz.png"
  width="200"
  title="Thin-walled profiles to illustrate the shear center">
](Linear/ShearCenter/)
[<img
  src="NonLinear/3PB/Refs/PEexpanded_yx.png"
  width="200"
  title="Three-point bending of a hollow profile, elastic-plastic">
](NonLinear/3PB/)
[<img
  src="Linear/Mesh1/Refs/shape_8.gif"
  width="200"
  title="Modal analysis of a plate with reinforced rim">
](Linear/Mesh1/)
[<img
  src="Thermal/Thermal shock/Refs/end_of_excitation.png"
  width="200"
  title="Deflection due to non-homogeneous thermal strain">
](Thermal/Thermal shock/)
[<img
  src="Contact/Penalty/contact.png"
  width="200"
  title="Experiment for testing pressure-penetration characteristics for various contact options">
](Contact/Penalty/)
