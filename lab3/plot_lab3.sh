#!/usr/bin/bash

gnuplot -persist <<-EOFMarker
    set terminal png size 1366,768 enhanced font 'Arial, 16'
    set output "${2}.png"

    set key top left
    set grid
    set xlabel "Math expectation sigma" font "Arial, 16"
    set ylabel "Math expectation omega" font "Arial, 16"
    set xtics font "Arial, 12"
    set ytics font "Arial, 12"

    plot "$1" using 1:2  title "0.1 Math expectation tau-sigma ${2} distribution" with linespoints ls 1,\
         "$1" using 1:3  title "0.2 Math expectation tau-sigma ${2} distribution" with linespoints ls 2,\
         "$1" using 1:4  title "0.3 Math expectation tau-sigma ${2} distribution" with linespoints ls 3,\
         "$1" using 1:5  title "0.4 Math expectation tau-sigma ${2} distribution" with linespoints ls 4,\
         "$1" using 1:6  title "0.5 Math expectation tau-sigma ${2} distribution" with linespoints ls 5,\
         "$1" using 1:7  title "0.6 Math expectation tau-sigma ${2} distribution" with linespoints ls 6,\
         "$1" using 1:8  title "0.7 Math expectation tau-sigma ${2} distribution" with linespoints ls 7,\
         "$1" using 1:9  title "0.8 Math expectation tau-sigma ${2} distribution" with linespoints ls 8,\
         "$1" using 1:10 title "0.9 Math expectation tau-sigma ${2} distribution" with linespoints ls 9
EOFMarker
