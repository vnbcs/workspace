outfile=HBN_missing_output.txt
echo -n "" >| $outfile

for subj in $(more ../HBN_missing_T1w_Freesurfer.txt); do
  subname="sub-"$subj
  subfold="proj-6199ab3e09959fabbd982c66"
  echo -n -e  "\n"$subj >> $outfile
  if [[ ! -d $subfold/$subname ]]; then
    echo -n -e "\tMISSING" >> $outfile
  elif [[ $(ls $subfold/$subname | wc -l) == "0" ]]; then
    echo -n -e "\tPARC-STATS MISSING" >> $outfile
  else
    echo -n -e "\tall good" >> $outfile
  fi
done

outfile=HBN_missing_output.txt
echo -n "" >| $outfile

for subj in $(cut -d , -f 1 ../../Phenotypic/HBN_R10.csv); do
  echo -n -e  "\n"$subj >> $outfile
  subname="sub-"$subj
  subfolds=("Site-CBIC/" "Site-CUNY/" "Site-RU/" "Site-SI/")
  for sf in ${subfolds[@]}; do
    if test -d $sf$subname; then
      echo -n -e "\t"$sf >> $outfile
    fi
  done
  echo -n -e "\n" >> $outfile
done


if test -d "Site-CBIC/sub-NDAREU890QQQ"; then echo "exists"; fi

for subj in $(ls *tar.gz); do
  tar -xvzf $subj
done
