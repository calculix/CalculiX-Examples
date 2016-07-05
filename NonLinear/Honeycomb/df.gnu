set term pngcairo
set grid
set xlabel "Displacement in mm"
set ylabel "Force in kN"
#set yrange [-100:100]
set nokey #
set key top left
set out "df.png"
plot "df.txt" using (-$8):(-$4*4) notitle w lp
