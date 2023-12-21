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
    # some of the subjects are already untarred
    # check for subj folder
    if [[ -d "$sub" ]]; then
	echo $dname
fi
done

# untar and delete as untarred
for file in *.tar.gz; do 
tar xzvf "${file}" && rm "${file}"; 
done
