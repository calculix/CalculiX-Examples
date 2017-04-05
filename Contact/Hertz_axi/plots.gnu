set term pngcairo enhanced
set title "Axisymmetric contact"
set grid
xc=60
set xlabel "Position along axis of symmetry in mm"
set ylabel "Stress in MPa"
set xrange [-10:10]
#set nokey
set key bottom right
set out "stress.png"
plot "sx.out" using ($2-xc):($3) title "{/Symbol s}_x" w l,\
     "sy.out" using ($2-xc):($3) title "{/Symbol s}_y" w l,\
     "sz.out" using ($2-xc):($3) title "{/Symbol s}_z" w l,\
     "mises.out" using ($2-xc):($3) title "{/Symbol s}_{EQ}" w l,\
     "maxshear.out" using ($2-xc):($3) title "{/Symbol t}_{max }" w l

set out "pres.png"
set title "Axisymmetric contact"
#set nokey
set xrange [0:5]
set yrange [0:5000]
set xlabel "Arc length from south pole in mm"
set ylabel "Contact pressure in MPa"
p(x)=4400*sqrt(1-x**2/2.92**2)
plot "pres.out" using ($2):($3) title "FEA" w lp , p(x) title "Theory"
