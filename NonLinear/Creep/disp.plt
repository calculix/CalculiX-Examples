set term pngcairo
set grid
set xlabel "Time in hr" 
set ylabel "Displacement in mm" 
set yrange [:] 
#set nokey 
set key top right 
set out "disp.png" 
plot 'displacements vx,vy,vz_NDISP.txt' using ($1/3600):5 w lp title 'Constant force' ,\
   'displacements vx,vy,vz_NDISP2.txt' using ($1/3600):5  w lp title 'Constant true stress' 