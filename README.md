# Extract FreeSurfer Cortex

The project extracts FreeSurfer cortex into OBJ format.

The OBJ format is general 3D format which is portable to other softwares,
like WebGL, Blender, Unity, ...

## Data Transformation

The visualization of the FreeSurfer Cortex is based on extraction the surface files.
To display the cortex in the surface manner,
there are at least **3** things we need

1. The 3D mesh of the cortex;
2. The feature value for the surface structure, like thickness, curvature, ...;
3. The functional activities across the cortex, which is basically from the other softwares, like `FSL`, `SPM`, ....

The `1st` and `2nd` features can be accessed through the `subjects` folder of the FreeSurfer.
Take the example of `fsaverage`,

1. The 3D mesh file is like `fsaverage/surf/lh.inflated`.
   It is a classic 3D OBJ file, but encoded by the FreeSurfer's private tools.
   It can be decoded as

   ```sh
   # The command converts the left hemisphere cortex into its ascii coded file
   fileName=$FREESURFER_HOME/fsaverage/surf/lh.inflated
   mris_convert $fileName $fileName.asc
   ```

   There are **vertex/positions** and **surface/cells** features in the file.
   The header of the file is like
   ```txt
   # Line1: Description of where the file is converted from
   # Line2: xxxx, yyyy
   #        xxxx refers the count of the vertex
   #        yyyy refers the count of the surface
   ```

2. The feature value specific to every vertex are restored in the files like `fsaverage/surf/lh.thickness`.
   To decode the file, the commands should work

   ```sh
   # The command converts the left hemisphere cortex's thickness values into ascii coded file
   # It requires template file to locate the vertex,
   # and the -C option refers the following file is scalar file.
   fileName=$FREESURFER_HOME/fsaverage/surf/lh.thickness
   tempName=$FREESURFER_HOME/fsaverage/surf/lh.white
   mris_convert -C $fileName $tempName $fileName.asc
   ```

   The values are listed in the file with the format of
   ```txt
   # Line1: 0000 xxxx yyyy zzzz value
   #        0000: The index of the vertex;
   #        xxxx | yyyy | zzzz: The x-, y-, z- position in the template file
   #        value: The value of the vertex.
   ```

3. Basically, the activities features are from different softwares.
   Currently, I only provide my another project to translate `FSL`'s `Zstat.nii.gz` files to the surface space.
   Please see my [GITHUB Page Reference](https://github.com/listenzcc/freesurferAnalysisScripts "GITHUB Page Reference") for details.

## Workshop

I have updated [Online Script](https://observablehq.com/@listenzcc/fsaverage-in-freesurfer "Online Scrip") to bed the projection.

## Developing Diary

### Code Improvement 1
The scripts have been **deprecated**,
not because they are bad.
But I have found better solution.

```md
## Scripts

-   The ./freesurfer2obj.sh script converts the cortex into OBJ format;
-   The ./srf2obj script provides the core functional of the converting;
-   The ./obj2csv.py script converts the OBJ format into vertex and surface files.

## Workshop

I have initialized [visualization project](https://observablehq.com/@listenzcc/free-surfer-cortex "visualization project") to the OBJ files.
```