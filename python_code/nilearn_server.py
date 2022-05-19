import os
import nibabel as nib
from nilearn import image as nimg
from nilearn import plotting as nplot
from nilearn import maskers
from nilearn.connectome import ConnectivityMeasure
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from tqdm import tqdm
import pickle

subj_folds = [x for x in os.listdir() if "." not in x]

pickled_batches = sorted([x for x in os.listdir() if x.endswith(".p")])

all_tups = []

print("loading batches...\n\n")

for e, x in enumerate(pickled_batches):
    all_tups.extend(pickle.load(open(x, "rb")))
    print("batch "+str(e)+" loaded\n")

yeo_7 = nimg.load_img('relabeled_yeo_atlas.nii.gz')

# each tup in all_tups contains confound_matrix, func_img, mask_img
masker = maskers.NiftiLabelsMasker(labels_img=yeo_7, standardize=True,
                                   memory='nilearn_cache', verbose=1, detrend=True,
                                   low_pass = 0.08, high_pass = 0.009, t_r=2)

print("\n\nmasking images...\n\n")
masked_imgs = []
success = []
for (confound_matrix, func, mask) in all_tups:
    try:
        masked = masker.fit_transform(func, confounds = confound_matrix)
        masked_imgs.append(masked)
        success.append(1)
    except:
        success.append(0)

correlation_measure = ConnectivityMeasure(kind='correlation')

print("\n\nfitting correlation matrix...\n\n")
correlation_matrix_all = correlation_measure.fit_transform(masked_imgs)

plt.figure(figsize=(7,5))
sns.heatmap(correlation_matrix_all[0], cmap='RdBu_r')
plt.title("all subjects")
plt.savefig("correlation_matrix_all.png")

correlation_matrix_1 = correlation_measure.fit_transform(masked_imgs[:47])
correlation_matrix_2 = correlation_measure.fit_transform(masked_imgs[47:])

fig, axs = plt.subplots(1, 2, figsize=(14, 5), sharey=False)
sns.heatmap(correlation_matrix_1[0], cmap='RdBu_r', ax=axs[0])
axs[0].set_title("first 47 subj")
sns.heatmap(correlation_matrix_2[0], cmap='RdBu_r', ax=axs[1])
axs[1].set_title("last "+str(len(masked_imgs)-47)+" subj")
plt.savefig("combined_matrix.png")
