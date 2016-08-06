set term pngcairo enhanced
set grid
set xlabel "Distance in mm"
set ylabel "{/Symbol s}_x in MPa"
set nokey
set key top left
set out "SXX-fix.png"
set title "Stress profile along support"
plot 0 notitle lc rgb "black",\
    "graph_0.out" using 2:3 title "First incr." w lp lc rgb "blue",\
    "graph_2.out" using 2:3 title "Last incr." w lp lc rgb "red"
set out "SXX-path.png"
set title "Stress profile at x=0 (eye position)"
plot 0 notitle lc rgb "black",\
        "graph_1.out" using 2:3 title "First incr." w lp lc rgb "blue",\
        "graph_3.out" using 2:3 title "Last incr." w lp lc rgb "red"
