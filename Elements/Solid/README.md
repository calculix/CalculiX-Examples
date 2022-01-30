## Simply Supported Beam Model With Solid Elements
Tested with CGX 2.19 / CCX 2.19

+ tetrahedral and hexahedral elements
+ linear or quadratic elements
+ full or reduced integration, incompatible shape functions

File                           | Contents    
:-------------                 | :------------- |
[solid.fbd](solid.fbd)         | Parametric pre- and postprocessing script for CGX   
[solid.inp](solid.inp)         | CCX input
[test.py](test.py)             | Python script to run the full example

Until version 2.15, this example had separate scripts for convergence study and for the plot. These have been directly integrated into `test.py`.

**Issue:** CGX 2.19 can't handle 4-node tetraeder elements with tetgen. Change line 708 of `generateTet.cpp` to

    if((body[nr].nod=(int *)realloc((int *)body[nr].nod, (set[setNr].anz_n+1)*sizeof(int)) )==NULL)
    

| Unstructured tet mesh    | structured hex mesh    |
| :------------- | :------------- |
| <img src="solid_C3D4_20_S.png" width="300"> |<img src="solid_C3D8I_20_S.png" width="300">

For the reference solution go to the [parent directory](https://github.com/mkraska/CalculiX-Examples/tree/master/Elements) of this example.

## Mesh Convergence of the Normalized Results

The function `solid_conv()` in `test.py` creates a data file for each element type with the mesh density parameter setting, the number of nodes and the maximum displacement and stress values. An example (C3D8I.txt):
```
# size NoN smax umax
200 8 0.046205 0.000108
100 12 0.077162 0.000151
50 30 0.089084 0.000164
20 264 0.093441 0.00017
10 1386 0.094022 0.000171
```
The function `solid_plot()` in `test.py` generates the following plot of the results normalized by the analytical reference values.

<img src="solid.svg" width="600">
