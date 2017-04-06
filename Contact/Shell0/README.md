# Shell Assembly
Tested with CGX/CCX 2.12

+ Shell edge to shell face connection
+ Various contact versions
+ Modal analysis

| File                   | Contents                                      |
| :-------------         | :-------------                                |
| [pre.fbd](pre.fbd)     | Pre-processing script for CGX                 |
| [pc-ns.inp](pc-ns.inp) | CCX input, node-to-surface penalty contact |
| [pc-ss.inp](pc-ss.inp) | CCX input, surface-to-surface penalty contact |
| [tie.inp](tie.inp)     | CCX input, MPC contact with `*tie`            |
| [equ.inp](equ.inp)     | CCX input, MPC contact with `*equation`       |

MPC contact with  `*tie` and penalty contact lead to a stiff connection betwenn shell edge to shell face. Node-to-surface penalty contact and MPC contact with `*tie` show similar behaviour. The frequencies for penalty contact are usually slightly lower than with MPC contact, which is plausible, as the penalty contact has added compliance.

Surface-to-surface contact gives frequencies which differ severely from the reference MPC contact. Also, for S8R elements, there are only 5 frequencies close to zero (should be 6 rigid body modes).

Penalty contact (both surface-to-surface and node-to-surface) requires the modal analysis being performed as a perturbation step with a preceeding static step (in the given case with no load applied). Note that the first result increment in a perturbation analysis is not a mode shape.

MPC contact with `*equation` leads to a hinged connection at shell edge to face contact (7 rigid body modes).


4x4 S4 elements

| Mode  | tie   | equ    | pc-ss   | pc-ns
| :--   | :--   | :--    | :--     | :--
| 1     | 0     | 0      | 0       | 0.013
| 2     | 0     | 0      | 0       | 0.038
| 3     | 0     | 0.047  | 0       | 0.043
| 4     | 0.0065| 0.088  | 0       | 0
| 5     | 0.084 | 0.102  | 0       | 0.079
| 6     | 0.090 | 0.103  | 0.034   | 0
| 7     | 1530  | 0.110  | 1322    | 1522
| 8     | 2846  | 2544   | 4001    | 2818
| 9     | 5543  | 3087   | 6769    | 5431
| 10    | 5648  | 4306   | 7422    | 5543

4x4 S8 elements (edit `pre.fbd` accordingly)

| Mode  | tie   | equ    | pc-ss   | pc-ns
| :--   | :--   | :--    | :--     | :--
| 1     | 0     | 0      | 0       | 0
| 2     | 0     | 0      | 0       | 0
| 3     | 0     | 0.     | 0       | 0
| 4     | 0     | 0      | 0.10    | 0
| 5     | 0.071 | 0      | 0.153   | 0.289
| 6     | 0.078 | 0.042  | 748     | 0
| 7     | 1468  | 0.184  | 1395    | 1405
| 8     | 2654  | 2408   | 2963    | 2629
| 9     | 3283  | 2798   | 3287    | 3222
| 10    | 4977  | 3996   | 5467    | 4827

4x4 S8R elements (edit `pre.fbd` accordingly)

| Mode  | tie   | equ    | pc-ss   | pc-ns
| :--   | :--   | :--    | :--     | :--
| 1     | 0     | 0      | 0       | 0.090
| 2     | 0     | 0      | 0       | 0.076
| 3     | 0     | 0.     | 0       | 0
| 4     | 0.022 | 0      | 0.077   | 0.147
| 5     | 0.042 | 0      | 0.151   | 0
| 6     | 0.117 | 0.071  | 1091    | 0
| 7     | 1402  | 0.077  | 1929    | 1358
| 8     | 2588  | 2393   | 2963    | 2579
| 9     | 3178  | 2750   | 3183    | 3122
| 10    | 4598  | 3847   | 3659    | 4529


## Preprocessing
Two separate parts are generated and meshed with shell elements.
```
> cgx -b pre.fbd
```
<img src="model.png" width="300">

## Solving
Use the appropriate input file  for the contact version you want to test:
```
> ccx tie
```

## Postprocessing

Load the results file in CGX
```
> cgx tie.frd
```
Display animated mode shapes coloured with the displacement magnitude. Show the elements and increase the default scaling of the mode shapes.
```
view elem
scal d 2
ds 1 a 4
```
Browse through the individual mode shapes using the PageDown and PageUp keys.

<img src="mode9.png" width="300">
