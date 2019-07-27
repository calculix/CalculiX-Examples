set term pngcairo
set grid
set xlabel "Global engineering strain in %"
set y2label "Strain in %"
set ylabel "Stress in MPa"
set yrange [0:*]
set y2tics
#set nokey
set key bottom right
set out "pe.png"
load "ez.gnu"
plot "graph_0.out" using ($3*ez*100):($5*100) title "Max. local eq. plastic strain" axes x1y2 w lp, \
"total force fx,fy,fz_NZ0.txt" using ($1*ez*100):(-$4/area) title "Global engineering stress" axes x1y1 w lp
