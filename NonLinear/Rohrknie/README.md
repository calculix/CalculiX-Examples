# Thin-Walled Tube
Tested with CGX 2.10 / CCX 2.9

+ Modal analysis
+ Shell model
+ Automatic movie generation in the post-processing

File                       | Contents    
 :-------------            | :-------------
 [values.fbd](values.fbd)  | CGX script, model parameters
 [geo.fbd](geo.fbd)        | CGX script, geometry plot
 [shell.fbd](shell.fbd)      | CGX script, pre-processing for the shell model    
 [shell-modal.fbd](shell-modal.fbd)      |  CGX-script, Complete  modal analysis of the shell model (including pre-post)
  [post-modal.fbd](post-modal.fbd)      |  CGX-script, Animation of mode shapes
 [shell-modal.inp](shell-modal.inp)  | CCX input, modal analysis, shell model

## Shell Model, Modal Analysis

In order to avoid inconsistent use of the individual scripts, top level script files are provided, which contain the calls to pre-processing, solving and post-processing.
```
> cgx -b shell-modal.fbd
```
<img src="Refs/geo-shell.png" width="400" title="Shell model">
<img src="Refs/shell-modal-1.gif" width="400" title="Mode 1">
