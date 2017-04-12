set term postscript landscape monochrom  
#set term x11 
set out "graph_3.ps"
set grid
set title "Values at Nodes (plots.fbl)"
set ylabel " T        "
set xlabel " Length "
plot "graph_3.out" using 2:3 title 'Setname Ntop1' with linespoints
