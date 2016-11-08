set term pngcairo
set grid
set xlabel "Engineering strain in %"
set ylabel "Nominal stress in MPa"
set yrange [0:*]
#set nokey
set key top left
set out "sigeps.png"
load "params.gnu"
plot "total force fx,fy,fz_NLOAD.txt" using ($1*maxe):($2/area) title "FEA" w l,\
     "Test 3.txt" using ($3/  0.8):($2/(25*8)) title "Test" w l
