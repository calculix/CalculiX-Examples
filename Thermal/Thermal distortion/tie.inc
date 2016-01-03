** surface definitions
*include, input=fdep.sur
*include, input=find.sur
*include, input=wdep.sur
*include, input=wind.sur
** contact definitions
*tie,name=seam_web
Swdep,Swind
*tie,name=seam_flange
Sfdep,Sfind
