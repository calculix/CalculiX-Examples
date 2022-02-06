set term pngcairo enhanced
set grid
set xlabel "time"
set ylabel "Force in N"
#set yrange [-100:100]
#set nokey
#set key top left
set out "surface_f.png"
plot "statistics_SFIX.txt" using 1:2 title "F_x" w lp,\
     "statistics_SFIX.txt" using 1:3 title "F_y" w lp,\
     "statistics_SFIX.txt" using 1:4 title "F_z" w lp,\
     "statistics_SFIX.txt" using 1:18 title "F_N" w lp,\
     "statistics_SFIX.txt" using 1:19 title "F_Q" w lp
set out "surface_m.png"
set ylabel "Moment in Nmm"
plot "statistics_SFIX.txt" using 1:5 title "M_{0x}" w lp,\
     "statistics_SFIX.txt" using 1:6 title "M_{0y}" w lp,\
     "statistics_SFIX.txt" using 1:7 title "M_{0z}" w lp,\
     "statistics_SFIX.txt" using 1:14 title "M_{Cx}" w lp,\
     "statistics_SFIX.txt" using 1:15 title "M_{Cy}" w lp,\
     "statistics_SFIX.txt" using 1:16 title "M_{Cz}" w lp
set out "surface_n.png"
set ylabel ""
set title "Surface normal components"
plot "statistics_SFIX.txt" using 1:11 title "n_{x}" w lp,\
     "statistics_SFIX.txt" using 1:12 title "n_{y}" w lp,\
     "statistics_SFIX.txt" using 1:13 title "n_{z}" w lp
set out #
