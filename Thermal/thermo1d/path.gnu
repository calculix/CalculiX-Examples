set term png
set out "path.png"
set grid
set title "Path plot for 3D model"
set ylabel "q in W/m^2"
set xlabel "x in m"
plot "graph_0.out" using 2:3 title 'averaged' with linespoints, \
     "graph_1.out" using 2:3 title 'non-averaged' with linespoints, 