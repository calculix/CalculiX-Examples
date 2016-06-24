set term pngcairo enhanced
set grid
set xlabel "Displacement in mm"
set ylabel "Force per length in N/mm"
set yrange [0:*]
#set nokey
#set key top left
set out "df.png"
plot "df.txt" using 6:2 w l
