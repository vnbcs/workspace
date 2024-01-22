All files have commented instructions at the top. Read the comments in addition to this file. 

Depending on the quantity of data, this may take a decent amount of time to run. I recommend using tmux or a job scheduler (i.e. slurm).

Requirements:
- Freesurfer-processed data
- [FSL (FMRIB Software Library)](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/) 
- [Python 3.10 (or greater)](https://www.python.org/)
    - [Required Python packages](https://github.com/estenhl/pyment-public/blob/main/requirements.txt)
- Local download of [`pyment-public`](https://github.com/estenhl/pyment-public)
- Singularity/Apptainer/Docker

1. Within your Freesurfer folder, run `bash STEP1_convert2nifti.sh`.
2. Create a folder for the pyment output. 
3. Run `python3.10 STEP2_cropniftis.py freesurfer_folder pyment_brainage`
    + If you are using a different version of Python (e.g. Python 3.11 or 3.12), replace `python3.10` with the appropriate version.
4. Create fake age labels OR create a CSV containing subject ages in the folder `pyment_brainage/cropped`. The file must be named `labels.csv`. To create fake age labels run: `python3.10 STEP3_fakeagelabels.py`
5. Within your pyment output folder, create a folder called `ba_preds`.
6. Within pyment output folder, run pyment.
    + If you are using Apptainer or Docker, change `singularity run` to the appropriate command.
```bash
    singularity run --mount type=bind,source=cropped,target=/images \
    --mount type=bind,source=ba_preds,target=/predictions \
    docker://estenhl/sfcn-reg-predict-brain-age
```

The predicted brainage can be found in `ba_preds/predictions.csv`.
