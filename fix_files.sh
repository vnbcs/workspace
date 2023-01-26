for file in ./*/*/*.nii.gz
do
  mv -- "$file" "${file%.nii.gz}.nii"
done

for file in ./*/*/*.nii
do
  mv -- "$file" "${file%.nii}.nii.gz"
done
