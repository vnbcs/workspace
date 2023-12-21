#!/bin/bash

# move to target directory

folds=(sub*);
for f in "${folds[@]}"; do
    niis=$(ls $f/anat/*.nii.gz)
    nii="${niis[0]}"
    jsons=$(ls $f/anat/*.json)
    json="${jsons[0]}"
    newnii=$(echo $nii | sed 's/_M.ID//')
    newjson=$(echo $json | sed 's/_M.ID//')
    mv $nii $newnii
    mv $json $newjson
done