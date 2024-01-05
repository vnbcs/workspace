#! /bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=28
#SBATCH --cluster=htc
#SBATCH --partition=htc
#SBATCH --time=24:00:00
#SBATCH --job-name=untarABCD

# move to abcd folder
cd /ix1/jhanson/abcd-mproc-release5/

for fold in *.tgz; do
    sub=$(echo $fold | cut -d"_" -f 1)
    if [[ -d "$sub" ]]; then # if subj folder already exists
	    rm "${fold}"; 
    else # if subject folder does not exist
        tar xzvf "${fold}" && rm "${fold}"; 
    fi
done