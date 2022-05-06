import os
from nilearn import image as nimg
from nilearn import plotting as nplot
import pandas as pd
import numpy as np
import nibabel as nib
from tqdm import tqdm
import pickle

serv = "/../Volumes/project/Hanson/"
fold = "Internal_MRI_Projects/CEDAR_MRI/Projects/nilearn_test/new_download"

def clean_img_dataloader(folder, subject):
    """
    Locate the required data to run nilearn.image.clean_img.
    Returns full filepaths for regressor file, functional image file, 
    and mask image file (if present). Technically not a data loader.
    
    folder and subject must be valid directories. 
    
    subject must contain files titled:
        regressors.tsv
        bold.nii.gz
    subject may optionally contain a file titled:
        mask.nii.gz
    """
    confounds = ""
    func = ""
    mask = ""
    
    for root,dirs,files in os.walk(folder + "/" + subject):
        for f in files:
            if "regressors.tsv" in f: 
                confounds+=(os.path.join(root, f))
            if "bold.nii.gz" in f: 
                func+=(os.path.join(root, f))
            if "mask.nii.gz" in f: 
                mask+=(os.path.join(root, f))
    
    if mask == "":
        return confounds, func
    
    else:
        return confounds, func, mask
    
def clean_img_prepdata(confounds, func, mask = None, derivatives = True, drop = 4,
                  confound_vars = ['trans_x','trans_y','trans_z','rot_x','rot_y','rot_z',
                                   'global_signal','csf', 'white_matter']):
    """
    Loads and prepares data for running through nilearn.image.clean_img.
    Returns confound matrix, functional image, and mask image (if present).
    
    derivatives is True by default. disable to reduce # of confound variables.
    
    drop is 4 by default. drops the first n timepoints from the data.
    
    confound_vars defaults to ['trans_x','trans_y','trans_z','rot_x','rot_y','rot_z',
                                   'global_signal','csf', 'white_matter'].
    if different confound_vars desired, they must be formatted as a list of strings. 
    strings must be valid column names in confounds file.
    
    """
    # prepare confounds
    confound_df = pd.read_csv(confounds, delimiter='\t')
    final_confounds = confound_vars
    
    if derivatives==True:
        final_confounds.extend(['trans_x_derivative1', 'trans_y_derivative1', 'trans_z_derivative1', 
                                'rot_x_derivative1', 'rot_y_derivative1', 'rot_z_derivative1',
                                'global_signal_derivative1','csf_derivative1','white_matter_derivative1'])
    
    confound_matrix = confound_df[final_confounds].loc[drop:].values
    
    raw_func_img = nimg.load_img(func)
    func_img = raw_func_img.slicer[:,:,:,drop:]
    
    if mask:
        mask_img = nimg.load_img(mask)
        return confound_matrix, func_img, mask_img
    
    else:
        return confound_matrix, func_img
    
def clean_img_batchload(folder, subj_list):
    """
    Locates, loads, and prepares data for running through nilearn.image.clean_img.
    Returns list containing tuples of confound matrix, functional image, and mask image (if present).
    """
    tup_list= []
    for s in tqdm(subj_list):
        c, f, m = clean_img_dataloader(folder, s)
        c_m, f_i, m_i = clean_img_prepdata(c, f, m)
        tup_list.append((c_m, f_i, m_i))
        
    return tup_list

subj_folds = [x for x in os.listdir(serv+fold) if "." not in x]
chunked_subj_folds = [subj_folds[i:i+10] for i in range(0, len(subj_folds), 10)]

all_tups = []

for e, batch in enumerate(chunked_subj_folds):
    print("\n\nrunning batch " + str(e + 1))
    tups = clean_img_batchload(serv+fold, batch)
    pickle.dump(tups, open("../files/CEDAR_processed_batch" + str(e+1) + ".p", "wb"))
    all_tups.extend(tups)
    
pickle.dump(all_tups, open("../files/CEDAR_processed_all.p", "wb"))
    

    
    