# Thermal Strain
Tested with CGX 2.16 / CCX 2.15

+ Transient coupled thermo-mechanical analysis
+ Bending of a plate due to one-sided heating
+ Time history plot of excitation and deflection
+ Cross thickness plot of temperature and stress

File                       | Contents    
 :-------------            | :-------------
 [pre.fbl](pre.fbl)        | CGX script, pre-processing
 [solve.inp](solve.inp)    | CCX input
 [post.fbl](post.fbl)      | CGX script, post-processing, images and plots
 [anim.fbl](anim.fbl)      | CGX script, movie
 [history.gnu](history.gnu)| Gnuplot script for the time history plot
 [profile.gnu](profile.gnu)| Gnuplot script for the profile plot
 [test.py](test.py)        | Python script to run the full simulation

The model represents a rectangular plate, which is supported in the center and exposed to a transient heat flux (excitation) at the upper side.

A cross-thickness temperature and stress gradient develops and remains for the duration of
the excitation time, leading to transient bending of the plate.

<img src="Refs/profile.png" width="400" title="Temperature and stress profile at the center of the plate"><img src="Refs/hist.png" width="400" title="Time history plot of the excitation and the tip deflection">

<img src="Refs/start.png" width="260" title="Deflection and temperature profile, initial state"><img src="Refs/end_of_excitation.png" width="260" title="Deflection and temperature profile at the end of the excitation"><img src="Refs/end.png" width="260" title="Deflection and temperature profile at the end of the simulation">


## Pre-Processing

Parameter | Value | Description
:--       | :--   | :---
`th`      | 2     | Thickness in mm
`wi`      | 20    | Width in mm
`le`      | 100   | Wength in mm

```
> cgx -b pre.fbl
```
The simulation domain is restricted to one quarter of the plate due to symmetry. It is meshed with 6 layers of C3D20R elements with cross thickness bias to capture the high gradients at the excitation side.

A set with a single node at the vertex of the plate is defined for history plot generation.

A node set marking a cross section path for plotting temperature and stress profiles is also defined.

<img src="Refs/mesh.png" width="400" title="Excitation surface (yellow), symmetry (red), history plot node (blue), profile path (magenta)"><img src="Refs/meshzoom.gif" width="400" title="Mesh with cross thickness bias">

## Solving

The analysis is done with the `*coupled temperature-displacement` procedure using
fixed time increments. During the excitation (approx. half of the total time), the convergence
is slightly slower than afterwards.
```
> ccx solve
> monitor.py solve
```

![solve.png](solve.png)

## Post-Processing

Create a time history animation of the deformed shape colored by the temperature:
```
> cgx -b anim.fbl
```
<img src="movie.gif" width="400" title="Animation of the temperature history">

```
> cgx -b post.fbl
```
creates the images used in the introduction above:
 1. a time history plot of the excitation intensity and the deflection of the plate tip
 2. a cross section temperature and stress profile plot
 4. Images of initial and final state and of the state at the end of the excitation.
