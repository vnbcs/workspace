!bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks-per-node=28
#SBATCH --cluster=smp
#SBATCH --time=24:00:00

# load modules
module load gcc/8.2.0 
module load python/anaconda3.10-2022.10

