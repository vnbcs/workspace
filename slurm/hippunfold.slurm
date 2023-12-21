! /bin/bash
#SBATCH --nodes=8
#SBATCH --ntasks-per-node=28
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=8:00:00
#SBATCH --job-name=HippunfoldTest1

module load singularity
module load gcc
module load python/anaconda3.10-2022.10

SIFILE=khanlab_hippunfold_latest.sif
RUNFILE=hippunfold/hippunfold/run.py
INFOLD=hippunfold_test
OUTFOLD=hippunfold_test/derivatives

singularity exec -e $SIFILE $RUNFILE $INFOLD $OUTFOLD participant -p --cores 8 --modality T1w --keep-going


