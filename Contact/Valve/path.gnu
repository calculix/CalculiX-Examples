set term pngcairo enhanced
set out "path.png"
set grid
set xlabel "Distance along path in mm"
set y2tics
set yrange [0:1600]
set y2range [0:0.16]
set ylabel "Pressure p in MPa"
set y2label "Sliding distance s in µm"
plot "graph_0.out" using 2:3 title "p" axes x1y1 w lp,\
"graph_1.out" using 2:($3*-1000) title "s" axes x1y2 w lp
