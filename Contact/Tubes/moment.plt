set yrange [0:*]
set xrange [0:*]
set xlabel "Time"
set ylabel "Moment in kNm"
set grid
set key bottom right
set term png
set out "moment.png"
plot "statistics_SLOAD.txt" using 1:($15/1000000) w lp
set out
