for subject in $(ls)
do
  echo $subject
  cort1=$subject/run-1/$subject"_cort_run-1.txt"
  cort2=$subject/run-2/$subject"_cort_run-2.txt"
  subcort1=$subject/run-1/$subject"_subcort_run-1.txt"
  subcort2=$subject/run-2/$subject"_subcort_run-2.txt"
  cort1feats=$subject/run-1/$subject"-1_cort_extracted-features.tsv"
  cort2feats=$subject/run-2/$subject"-2_cort_extracted-features.tsv"
  subcort1feats=$subject/run-1/$subject"-1_subcort_extracted-features.tsv"
  subcort2feats=$subject/run-2/$subject"-2_subcort_extracted-features.tsv"
  python ../ts_features.py $cort1 $cort1feats
  python ../ts_features.py $cort2 $cort2feats
  python ../ts_features.py $subcort1 $subcort1feats
  python ../ts_features.py $subcort2 $subcort2feats
done
