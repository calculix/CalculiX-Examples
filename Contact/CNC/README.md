# Multipart Assembly

Tested with CGX 2.19 / CCX 2.19

+ Assembly of mesh parts
+ Parametric parts generated in CGX
+ Assembly is non-parametric
+ Automatic contact detection (ACD)

File                          | Contents                                      
:-------------                | :-------------                                
[assembly.fbd](assembly.fbd)  | Top level CGX script                 
[profile.fbd](profile.fbd)    | CGX script for slot profile                 
[winkel.fbd](winkel.fbd)      | CGX script for angle bracket                 
[SK.fbd](SK.fbd)              | CGX script for SK bracket                
[rod.fbd](rod.fbd)            | CGX script for 8mm rod                
[post.fbd](post.fbd)          | CGX script postprocessing             
[solve.inp](solve.inp)        | CCX input   
[test.py](test.py)            | Python script to run the complete simulation  

# Parts

Generate the parts:
```
> cgx -b profile.fbd
> cgx -b winkel.fbd
> cgx -b SK.fbd
> cgx -b rod.fbd
```

<img src="Refs/profile.png" width="400" title="Profile"><img src="Refs/winkel.png" width="400" title="Bracket">                                     
<img src="Refs/SK.png" width="400" title="Clamp"><img src="Refs/rod.png" width="400" title="Rod">                              

# Assembly

```
> cgx -b assembly.fbd
```

The part meshes are read, copied, translated, rotated and sometimes scaled. If contact is required, the parts touch each other without gap.

<img src="Refs/parts.png" width="600" title="Assembly">

The CGX command `neigh` generates the contact surfaces and the contact definitions for CCX based on face-to-face proximity. `*tie` MPC contact is used.

<img src="Refs/contact.png" width="600" title="Contact pairs">

In order to verify correct bonding of the parts, a modal analysis is performed. No displacement constraints (supports) are applied.

```
> ccx solve
```
The postprocessing script shows the eigenmodes:

```
> cgx -b post.fbd
```
<img src="Refs/shape_7.gif" width="400" title="Mode 7"><img src="Refs/shape_8.gif" width="400" title="Mode 8">
<img src="Refs/shape_9.gif" width="400" title="Mode 9"><img src="Refs/shape_10.gif" width="400" title="Mode 10">
