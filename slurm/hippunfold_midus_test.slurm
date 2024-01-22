#!/bin/bash
#SBATCH --account=jhanson
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=8:00:00
#SBATCH --output=abcd_logfiles/MIDUS-%j.out 
#SBATCH --job-name=MidusHippTest2

module load singularity

SIFILE=../khanlab_hippunfold_latest.sif
INFOLD=midus_test2
OUTFOLD=midus_test2/derivatives/hippunfold

singularity run -e $SIFILE $INFOLD $OUTFOLD \
participant -p --cores 8 --modality T1w --keep-going --force-output