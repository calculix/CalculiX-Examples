set term pngcairo enhanced
set out "Refs/hist.png"
set key top right
set grid
set xlabel "Time in s"
set ylabel "Intensity in %"
set yrange [-10:110]
set y2label "Deflection in {/Symbol m}m"
set y2range [-5:50]
set y2tics
plot "excite.out" using 2:($3*100) axes x1y1 title "Excitation" w l,\
"graph_0.out" using 3:($5*1000) axes x1y2 title "Tip deflection" w l lt 3
