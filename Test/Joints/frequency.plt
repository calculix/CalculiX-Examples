set term pngcairo
set style fill solid 
set grid
set xlabel "Mode #"
set ylabel "Frequency in Hz"
set boxwidth 0.3 
set yrange [0:*] 
set nokey
#set key top left
set out "f.png"
plot "Eigenvalues_1.txt" using 1:4 w boxes fc rgb "red"
set out #
