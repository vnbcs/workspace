#!/bin/bash
#SBATCH --account=jhanson
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=28
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=24:00:00
#SBATCH --job-name=HippunfoldMidus

module load singularity

SIFILE=khanlab_hippunfold_latest.sif
INFOLD=MIDUS
OUTFOLD=MIDUS/derivatives/midus_hippunfold

singularity run -e $SIFILE $INFOLD $OUTFOLD \
participant -p --cores 8 --modality T1w --keep-going --force-output