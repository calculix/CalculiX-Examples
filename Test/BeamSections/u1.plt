set term pngcairo
set out "Refs/u1-def.png"
set xlabel "Node number"
plot "u1.txt" using 1:4 title "UZ" w lp, \
"u1.txt" using 1:6 title "RY" w lp
