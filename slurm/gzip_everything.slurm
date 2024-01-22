#! /bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=28
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=24:00:00
#SBATCH --job-name=gzipABCD

find abcd-mproc-release5 -type f -name "*.nii" -exec gzip {} \;