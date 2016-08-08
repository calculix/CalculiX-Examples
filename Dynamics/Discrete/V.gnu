set term pngcairo enhanced
# mode shapes
set out "modes.png"
set key top left
set grid
set ylabel "Amplitude (unitless)"
plot "graph_0.out" using 2:3 title "Mode 1" w lp, "graph_1.out" using 2:3 title "Mode 2" w lp
set out "V.png"
set multiplot layout 2,1 title "Displacement response"
set key top left
set grid
#set xlabel "Frequency in Hz"
set ylabel "Magnitude in mm"
set yrange [0:1]
plot "graph_response_PDISP_MAG1.out" using 1:3 title "M1" w lp, "" using 1:5 title "M2" w lp
set xlabel "Frequency in Hz"
set ylabel "Phase in °"
set yrange [*:*]
set ytics 90
set nokey
plot "graph_response_PDISP_PHA1.out" using 1:3 title "M1" w lp, "" using 1:5 title "M2" w lp
