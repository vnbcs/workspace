#!/bin/bash
#SBATCH --account=jhanson
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=28
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=8:00:00
#SBATCH --job-name=HippunfoldTest1

module load singularity

SIFILE=khanlab_hippunfold_latest.sif
INFOLD=hippunfold_test
OUTFOLD=hippunfold_test/derivatives

singularity run -e $SIFILE $INFOLD $OUTFOLD \
participant -p --cores 8 --modality T1w --keep-going



