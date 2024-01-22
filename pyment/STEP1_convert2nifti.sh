#!bin/bash

# pyment step 1: convert some freesurfer files to niftis
# run freesurfer first! 
# requires working installation of FSL (FMRIB Software Library)

# instructions:
# run this file WITHIN freesurfer output folder. by default the folder should be titled something like Freesurfer_7. folder name does not matter for this script.
#	> cd Freesurfer_7
#	> bash /path/to/this/file/STEP1_convert2nifti.sh

# this script WILL use 100% of all available processing power on your machine so i recommend running it on a server OR using a job scheduler (i.e. slurm) to limit the available cores.

subs=($(find . -type d -name 'sub*'))
sub_count=$(echo "${subs[@]}" | wc -w)

process_sub() {
	sub=$1
	if [[ ! -f $sub"/mri/brainmask_reorient_MNI.nii.gz" ]]; then
		mri_convert $sub"/mri/brainmask.mgz" \
		$sub"/mri/brainmask.nii.gz" -ot nii;
		fslreorient2std $sub"/mri/brainmask.nii.gz" \
		$sub"/mri/brainmask_reorient.nii.gz";
		flirt -dof 6 -in $sub"/mri/brainmask_reorient.nii.gz" \
		-ref /usr/share/fsl/5.0/data/standard/MNI152_T1_1mm_brain.nii.gz \
		-out $sub"/mri/brainmask_reorient_MNI.nii.gz"
	fi
}

export -f process_sub
for s in "${subs[@]}"; do
	sem -j +0 process_sub $s
	echo "process $s terminated"
done
sem --wait