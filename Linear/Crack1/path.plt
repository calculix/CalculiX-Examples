set term pngcairo enhanced
set out "Refs/path.png"
set key top left
set grid
set xlabel "Distance from back side in mm"
set ylabel "Normal stress in MPa"
set yrange [-5:10]
set y2label "Crack opening in {/Symbol m}m"
set y2range [-0.5:1]
set y2tics
plot "graph_0.out" using 2:3 axes x1y1 title "stress" w l,\
     "graph_1.out" using 2:($3*1000) axes x1y2 title "displacement" w l
