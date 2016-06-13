set term pngcairo enhanced
set out "Refs/profile.png"
set key top right
set title "Cross thickness profile at end of excitation"
set grid
set xlabel "Distance in mm"
set ylabel "{/Symbol D}T in K"
set yrange [-1:2]
set y2label "Stress in MPa"
set y2range [-1:2]
set y2tics
plot "graph_1.out" using 2:3 axes x1y1 title "{/Symbol D}T" w l,\
"graph_2.out" using 2:3 axes x1y2 title "{/Symbol s}_{zz}" w l lt 3
