set term postscript landscape monochrom  
#set term x11 
set out "graph_0.ps"
set title "Values at Nodes (post.fbl)"
set grid
set ylabel " D1       "
set xlabel " Time "
plot "graph_0.out" using 3:5 title 'Node=498' with linespoints
 