#!/bin/sh

# How to use:
# - mkSubject fsaverage $FREESURFER_HOME lh

# What will happen:
# The ASC file of the [hemi]-[subject] of freesurfer file will be created
# and saved in the `src/[subject]` folder.

# Additionally, the folder of `csv/[subject]` will be generated for the next step.

# Input parameters
subject=$1
freesurfer=$2
hemi=$3

echo ---- Making subject: $subject ----

dir=$freesurfer/subjects/$subject
src=src/$subject

mkdir $src -p
mkdir csv/$subject -p

mris_convert $dir/surf/$hemi.pial $src/$hemi.pial.asc
mris_convert $dir/surf/$hemi.inflated $src/$hemi.inflated.asc
mris_convert $dir/surf/$hemi.sphere $src/$hemi.sphere.asc

mris_convert -C $dir/surf/$hemi.thickness $dir/surf/$hemi.white $src/$hemi.thickness.asc
mris_convert -C $dir/surf/$hemi.sulc $dir/surf/$hemi.white $src/$hemi.sulc.asc
mris_convert -C $dir/surf/$hemi.curv $dir/surf/$hemi.white $src/$hemi.curv.asc

echo Done with $subject, $dir
