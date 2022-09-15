cort=HarvardOxford-cort-maxprob-thr50-2mm.nii.gz
subcort=HarvardOxford-sub-maxprob-thr50-2mm.nii.gz

for subject in $(ls subs)
do
   run1file=$(ls subs/$subject/run-1)
   run2file=$(ls subs/$subject/run-2)
   echo "running subject:$subject ---------------"
   # cortical parcellation
   python extract_timeseries.py subs/$subject/run-1/$run1file $cort subs/$subject/run-1$subject_extracted_timeseries_run-1.txt
   python extract_timeseries.py subs/$subject/run-2/$run1file $cort subs/$subject/run-2$subject_extracted_timeseries_run-2.txt

   #subcortical parcellation
   python extract_timeseries.py subs/$subject/run-1/$run1file $subcort subs/$subject/run-1$subject_extracted_timeseries_run-1.txt
   python extract_timeseries.py subs/$subject/run-2/$run1file $subcort subs/$subject/run-2$subject_extracted_timeseries_run-2.txt
done

python extract_timeseries.py subs/NDARDX173WLD/run-1/bold.nii.gz $cort subs/NDARDX173WLD/run-1/NDARDX173WLD_extracted_timeseries_run-1.txt
