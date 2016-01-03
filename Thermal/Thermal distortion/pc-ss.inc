** surface definitions
*include, input=fdep.sur
*include, input=find.sur
*include, input=wdep.sur
*include, input=wind.sur
** contact definitions
*surface interaction, name=tie
*surface behavior, pressure-overclosure=tied
1e7
*friction
1,1e7
*contact pair, interaction=tie, type=surface to surface
Swdep,Swind
Sfdep,Sfind
