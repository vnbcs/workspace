# pyment step 2: crop the niftis
# code adapted from:
# https://github.com/estenhl/pyment-public/blob/main/notebooks/Download%20and%20preprocess%20IXI.ipynb

# requires working installation of python version >=3.10
# download folder pyment-public from github: https://github.com/estenhl/pyment-public
# install the following python packages: https://github.com/estenhl/pyment-public/blob/main/requirements.txt
# conveniently (sarcasm) the pyment folks do not specify the versions of the packages.
# you might have versioning problems? i don't remember. if you have versioning problems... first contact your sysadmin. then contact me. 

# (note: you can also use a python virtual environment if you know how to do that. i do *not* recommend learning how to use virtual envs for this project specifically. your local install should be fine.)

# instructions: 
# edit line 24 of this file!!!! the line must point to *your local pyment-public folder*
# make a folder for your pyment output. i usually name it "pyment_brainage"
# run the following
#   > python3.10 path/to/this/file/STEP2_cropniftis.py path/to/folder/Freesurfer_7 path/to/folder/pyment_brainage

import sys, os
fs_folder = sys.argv[1]
dest_folder = sys.argv[2]

# CHANGE THIS LINE
sys.path.insert(0, '/path/to/folder/pyment-public') # <<<<<<<< CHANGE THIS!!!!

from pyment.utils.preprocessing import crop_mri

bounds = ((6, 173), (2, 214), (0, 160))
subs = os.listdir(fs_folder)
subs = [x for x in subs if x.startswith('sub')]

sub_niis = [(fs_folder + '/' + x + '/mri/brainmask_reorient_MNI.nii.gz', dest_folder + '/cropped/images/' + x.replace('.','-') + '_final_cropped.nii.gz') for x in subs]

if not os.path.exists(dest_folder + '/cropped/images/'):
    os.makedirs(dest_folder + '/cropped/images/')

for f_src, f_dst in sub_niis:	
	# print(f_src, f_dst)
	if os.path.exists(f_src) and not os.path.exists(f_dst):
		crop_mri(f_src, f_dst, bounds)