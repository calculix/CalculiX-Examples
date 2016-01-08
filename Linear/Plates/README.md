# Axisymmetric Plate With Holes
Tested with CGX 2.10/CCX 2.9

+ Linear static solution
+ Axisymmetric model
+ Test of expansion sweep in the post-processing for various element types
+ Demonstration of polar co-ordinate system for stress components

File                    | Contents    
 :-------------         | :-------------
 [pre.fbd](pre.fbd)     | Pre-processing script for CGX     
 [post.fbd](post.fbd)   | Post-processing script for CGX
 [plates.inp](plates.inp) | CCX input

## Preprocessing
```
cgx -b pre.fbd
```
<img src="mesh.png" width="300" title="Disks with different element types. Centerline added just for clarity">

## Solving
```
ccx plates
```

## Postprocessing
```
cgx -b post.fbd
```

<img src="polar.png" width="300" title="Expanded model, radial normal stress SRR"> <img src="2D3Dpng" width="300" title="Expanded model with just the base region coloured">

![cuty0.png](cuty0.png)
