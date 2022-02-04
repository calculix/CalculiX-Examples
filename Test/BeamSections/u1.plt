set term pngcairo
set out "Refs/u1-3-def.png"
set xlabel "Node number"
set grid
set title "Load in z (local 2)-direction"
plot "u1-3.txt" using 1:4 title "UZ" w lp, \
"u1-3.txt" using 1:6 title "RY" w lp
set out "Refs/u1-2-def.png"
set xlabel "Node number"
set grid
set title "Load in y (local 1)-direction"
plot "u1-2.txt" using 1:3 title "UY" w lp, \
"u1-2.txt" using 1:6 title "RZ" w lp
