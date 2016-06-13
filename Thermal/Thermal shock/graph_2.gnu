set term postscript landscape monochrom  
#set term x11 
set out "graph_2.ps"
set grid
set title "Values at Nodes (post.fbl)"
set ylabel " SZZ      "
set xlabel " Length "
plot "graph_2.out" using 2:3 title 'Setname NNpath' with linespoints
