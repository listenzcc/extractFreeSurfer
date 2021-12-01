#!/bin/sh

fname=$1

echo ---- Convert Free Surfer to OBJ format ---------------------------
echo Working with $fname

mris_convert $fname $fname.asc

ln -vrs $fname.asc $fname.srf

./srf2obj $fname.srf > $fname.obj

echo Done with $fname
