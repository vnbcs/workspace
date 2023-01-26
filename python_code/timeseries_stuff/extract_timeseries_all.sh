cort=HarvardOxford-cort-maxprob-thr50-2mm.nii.gz
subcort=HarvardOxford-sub-maxprob-thr50-2mm.nii.gz

for subject in $(ls subs)
do
   run1file=$(ls subs/$subject/run-1/*.nii.gz)
   run2file=$(ls subs/$subject/run-2/*.nii.gz)
   echo "running subject:$subject ---------------"
   # cortical parcellation
<<<<<<< HEAD
   python extract_timeseries.py "$run1file" $cort "subs/$subject/run-1/$subject_extracted_timeseries_run-1_cort.txt"
   python extract_timeseries.py "$run1file" $cort "subs/$subject/run-2/$subject_extracted_timeseries_run-2_cort.txt"

   #subcortical parcellation
   python extract_timeseries.py "$run1file" $subcort "subs/$subject/run-1/$subject_extracted_timeseries_run-1_subcort.txt"
   python extract_timeseries.py "$run1file" $subcort "subs/$subject/run-2/$subject_extracted_timeseries_run-2_subcort.txt"
done

# python extract_timeseries.py subs/NDARDX173WLD/run-1/bold.nii.gz $cort subs/NDARDX173WLD/run-1/NDARDX173WLD_extracted_timeseries_run-1.txt
=======
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
>>>>>>> 81fda333a0e1442f1afa88b3e529271de3c806e2
