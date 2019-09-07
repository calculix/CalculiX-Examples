# Wire Bending
Tested with CGX 2.16 / CCX 2.15

Click the image to see the animation

<img src="movie.gif" width="400">

+ Large displacements
+ Plasticity
+ Contact (smoothed bi-linear node-to-surface)
+ Rigid body with prescribed rotation

| File     | Contents    |
| :------------- | :------------- |
| [pre.fbd](pre.fbd)     | Pre-processing script for CGX     |
| [post.fbd](post.fbd) | Post-processing script for CGX |
| [Biegung.inp](Biegung.inp) | CCX input |
| [Biegung.py](Biegung.py) | Python script for history plot |
| [Animation.fbd](Animation.fbd) | CGX script to produce the animation |
| [test.py](test.py) | Python script for test run of the example |

## Reference Estimates
Click the image below to open a life SMath worksheet

[![Screenshot](Wire%20bending.png)](http://smath.info/cloud/worksheet/34vUp7hs)

## Preprocessing

The parameters can be changed in `pre.fbd`.

| Parameter | Value | Meaning |
| :------------- |  :------------- | :------------- |
| `R` | 1 | radius of the wire in mm |
| `L` | 16 | length of the wire in mm |
| `R1` | 5 | radius of the fixed tool (die) in mm |
| `R2` | 2 | radius of the movable tool in mm |
| `X`  | 5 | x-position of the center of the die (point A) in mm |
| `Phi1` | 120 | sector angle of the die surface in ° |
| `DivR` | 2 | number of radial mesh segments in the wire |
| `DivL` | 40 | number of longitudinal mesh segments in the wire |
| `Div1` | 40 | number of circumferential mesh segments in the die |
| `Div2` | 20 | number of circumferential mesh segments in the movable tool |

```
> cgx -b pre.fbd
```
Node sets

<img src="symy.png" width="300"><img src="wfix.png" width="300">

Parts and contact surfaces

<img src="parts.png" width="300"><img src="contact.png" width="300">

## Solving

```
> ccx Biegung
> monitor.py Biegung
```
<img src="Biegung.png">

## Postprocessing

Extraction of the time history of the reaction moment and the internal energy from the dat file and generation of the corresponding plot
```
> dat2txt.py Biegung
> Biegung.py
```
<img src="Biegung-history.png">

When comparing to the reference solution take care that the FEA model is just half of the wire (symmetry).

| Quantity       | Reference          | 2xFEA     |
| :------------- | :-------------     |:---       |
| Moment in N mm | 980                | 800...920 |
| Energy in mJ   | 1290               | 1040      |

The matching is reasonable, given the crude approach for the reference estimates and the coarse mesh.

Create the animation (see on the top of this page)
```
cgx -b Animation.fbd
```
Open the results in CGX and create some plots
```
cgx -b post.fbd
```
<img src="deform.png" width="300"><img src="PE.png" width="300">
