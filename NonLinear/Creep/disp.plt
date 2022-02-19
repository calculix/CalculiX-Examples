set term pngcairo
set grid
set xlabel "Time in hr" 
set ylabel "Displacement in mm" 
set yrange [:10] 
set nokey 
#set key top left 
set out "disp.png" 
plot 'displacements vx,vy,vz_MONITOR.txt' using ($1/3600):5 w lp