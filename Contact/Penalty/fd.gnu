set term png
set grid
set xlabel "Penetration in mm"
set ylabel "Force in kN"
#set yrange [-100:100]
set nokey
#set key top left
set out "fd.png"
plot "total force fx,fy,fz_NKW.txt" using ($1/5-0.3):($2/1000) w lp
