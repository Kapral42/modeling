#!/usr/bin/bash

rm -f *.png
rm -f *.out
./lab3.py
list=`ls | grep .out`
for l in $list ; do
    title=`echo $l | sed 's/_/-/g' | sed 's/.out//g'`
    #echo $title
    ./plot_lab3.sh $l $title
done
