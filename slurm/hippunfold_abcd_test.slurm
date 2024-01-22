#!/bin/bash
#SBATCH --account=jhanson
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=8:00:00
#SBATCH --output=abcd_logfiles/slurm-%j.out 
#SBATCH --job-name=ABCDHippTest

module load singularity

SIFILE=../khanlab_hippunfold_latest.sif
# INFOLD=abcd-mproc-release5
INFOLD=abcd_test2
OUTFOLD=abcd_test2/derivatives/hippunfold

singularity exec -e $SIFILE $INFOLD $OUTFOLD participant -p --cores 8 --modality T1w --keep-going --force-output

# singularity exec -e $SIFILE $INFOLD $OUTFOLD \
# participant -p --cores 8 --modality T1w \
# --participant-label NDARINV003RTV85 NDARINV005V6D2C NDARINV007W6H7B \
# --keep-going --force-output


