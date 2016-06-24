set term pngcairo enhanced
set title "Plane strain contact, displacement control"
set grid
xc=60
set xlabel "Normal distance from center in mm"
set ylabel "Stress in MPa"
set xrange [-10:10]
#set nokey
#set key top left
set out "dc-stress.png"
plot "dc-sx.out" using ($2-xc):($3) title "{/Symbol s}_x" w l,\
     "dc-sy.out" using ($2-xc):($3) title "{/Symbol s}_y" w l,\
     "dc-sz.out" using ($2-xc):($3) title "{/Symbol s}_z" w l,\
     "dc-mises.out" using ($2-xc):($3) title "{/Symbol s}_{EQ}" w l,\
     "dc-maxshear.out" using ($2-xc):($3) title "{/Symbol t}_{max }" w l
set out "pc-stress.png"
set title "Plane strain contact, pressure control"
plot "pc-sx.out" using ($2-xc):($3) title "{/Symbol s}_x" w l,\
     "pc-sy.out" using ($2-xc):($3) title "{/Symbol s}_y" w l,\
     "pc-sz.out" using ($2-xc):($3) title "{/Symbol s}_z" w l,\
     "pc-mises.out" using ($2-xc):($3) title "{/Symbol s}_{EQ}" w l,\
     "pc-maxshear.out" using ($2-xc):($3) title "{/Symbol t}_{max }" w l

set out "dc-pres.png"
set title "Plane strain contact, displacement control"
set nokey
set xrange [0:20]
set xlabel "Transverse distance from center in mm"
set ylabel "Contact pressure in MPa"
plot "dc-pres.out" using ($2):($3) w l
set out "pc-pres.png"
set title "Plane strain contact, pressure control"
set nokey
set xrange [0:20]
set ylabel "Contact pressure in MPa"
plot "pc-pres.out" using ($2):($3) w l
