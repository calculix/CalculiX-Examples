set term pngcairo
set grid
set xlabel "Time in hr" 
set ylabel "Creep strain in %" 
set yrange [:] 
#set nokey 
set key top right
set out "peeq.png" 
plot 'equivalent plastic strain elem, integ.pnt.,pe_EPEEQ.txt' using ($1/3600):($4*100) w lp title 'Constant force' ,\
   'equivalent plastic strain elem, integ.pnt.,pe_EPEEQ2.txt' using ($1/3600):($4*100) w lp title 'Constant true stress'  