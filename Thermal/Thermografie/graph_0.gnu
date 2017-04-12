set term postscript landscape monochrom  
#set term x11 
set out "graph_0.ps"
set title "Values at Nodes (plots.fbl)"
set grid
set ylabel " T        "
set xlabel " Time "
plot "graph_0.out" using 3:5 title 'Node=495' with linespoints, "graph_0.out" using 3:6 title 'Node=510' with linespoints, "graph_0.out" using 3:7 title 'Node=3711' with linespoints, "graph_0.out" using 3:8 title 'Node=3741' with linespoints
 