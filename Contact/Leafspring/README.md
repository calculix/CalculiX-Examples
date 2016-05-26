# Leaf Spring
Tested with CGX/CCX 2.10

+ Parametric model with variable number of leafs
+ completely automatic generation of the solver input using a loop in CGX
+ Penalty contact
+ Static analysis
+ Analysis of a quarter model, expanded in postprocessing

| File                   | Contents                                      |
| :-------------         | :-------------                                |
| [pre.fbd](pre.fbd)     | Pre-processing script for CGX                 |
| [solve.inp](solve.inp) | CCX input                                     |
| [post.fbd](post.fbd)   | Post-processing                               |

The main feature of this model is the automatic generation of a given number of
spring leafs along with the required contact definitions.

In the file `pre.fbd` you can set the following parameters:

| Name                   |                                       |
| :-------------         | :-------------                                |
| L    | Half-span                |
| W    | Half-width                                   |
| T    | Tickness of the leafs                        |
| num  | Number of leafs |

## Preprocessing

Run
```
> cgx -b pre.fbd
```
<img src="Refs/geo.png" width="300">

Boundary conditions:
* ux=0 at x=0 (symmetry)
* uy=0 at y=0 (symmetry)
* uz=10 at x=0 (displacement-controlled load)
* uz=0 at x=L and z=(num-1) * W (support at the end of the upper leaf)

Between the leafs, node-to-surface penalty contact is used. The contact parameters
were basically just guessed, thus there is plenty of room for systematic studies.

## Solving

```
> ccx solve
> ../../Scripts/monitor.py solve
```
<img src="solve.png">

## Postprocessing

```
> cgx -b post.fbd
```
Display of the bending stress in the model domain and symmetry expansion.

<img src="Refs/Sxx.png" width="300">
