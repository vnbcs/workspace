cort=HarvardOxford-cort-maxprob-thr50-2mm.nii.gz
subcort=HarvardOxford-sub-maxprob-thr50-2mm.nii.gz

for subject in $(ls subs)
do
   run1file=$(ls subs/$subject/run-1/*.nii.gz)
   run2file=$(ls subs/$subject/run-2/*.nii.gz)
   echo "running subject:$subject ---------------"
   # cortical parcellation
   # run-1
   if [[ ! -f subs/$subject/run-1/cort_run-1.txt ]]; then
     python extract_timeseries.py $run1file $cort subs/$subject/run-1/cort_run-1.txt
   fi
   # # run-2
   if [[ ! -f subs/$subject/run-2/cort_run-2.txt ]]; then
     python extract_timeseries.py $run2file $cort subs/$subject/run-2/cort_run-2.txt
   fi

   #subcortical parcellation
   # run-1
   if [[ ! -f subs/$subject/run-1/subcort_run-1.txt ]]; then
     python extract_timeseries.py $run1file $subcort subs/$subject/run-1/subcort_run-1.txt
   fi
   # run-2
   if [[ ! -f subs/$subject/run-2/subcort_run-2.txt ]]; then
     python extract_timeseries.py $run2file $subcort subs/$subject/run-2/subcort_run-2.txt
   fi
done
