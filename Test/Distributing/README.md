# Stress distribution with distributing coupling

Tested with CGX 2.13.1 / CCX 2.13

+ Test of distributing coupling
+ Stress distribution for applied moments
+ Issue: Moment about x doesn't generate any stress with CCX 2.13, see [results for CCX 2.12](https://github.com/mkraska/CalculiX-Examples/tree/v2.12/Test/Distributing)


File                          | Contents    
:-------------                | :-------------
[run.fbl](run.fbl)            | CGX script, full simulation
[solve.inp](solve.inp)        | CCX input
[path.gpl](path.gpl)          | Gnuplot input for path plots
[test.py](test.py)            | Python script to run the full simulation

The model consists of a thin rectangular plate. The bottom at z=0 is fixed (all dofs constrained).
To the upper surface, moments are applied via distributing coupling.

For path plots of the stress distribution, appropriate node sets are generated.

The plots of the normal stress show the load distribution for bending moments, the plots of the max shear stress show the load distribution in torsion.


```
> cgx -b run.fbl

```
Application of the moment about x in step 1 seems to fail in CCX 2.13 (worked in CCX 2.12). No stress is generated in this case. Also, the section print results indicate the lack of any loads in this step.

<img src="Refs/mx.png" width="400"><img src="Refs/my.png" width="400">
<img src="Refs/mz-disp.png" width="400"><img src="Refs/mesh.png" width="400">

The stress profiles are hyperbolic with distance from the center of gravity (a linear distribution would be expected)

<img src="Refs/stress.png">
