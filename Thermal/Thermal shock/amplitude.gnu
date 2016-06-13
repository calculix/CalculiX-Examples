set term postscript landscape monochrom  
#set term x11 
set out "amplitude.ps"
set grid
set title "Amplitude"
set ylabel " y "
set xlabel " x "
plot "excite.out" using 2:3 title 'excite' with linespoints
