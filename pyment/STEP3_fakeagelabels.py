# step 3ish: make fake age labels
# pyment requires there be an age labels. this file makes a CSV of random ages between 10 and 70 
# you can provide accurate age labels if you want! pyment doesn't actually use the age labels at all. 

# instructions
# run within your pyment output folder
#   > cd pyment_brainage
#   > python3.10 /path/to/this/file/STEP3_fakeagelabels.py

import os
import pandas as pd
import numpy as np

subs = os.listdir('cropped/images')
subs = [x[:-7] for x in subs]

fake_age_df = pd.DataFrame()

fake_age_df['id'] = subs

rng = np.random.default_rng()
fake_age_df['age'] = rng.integers(10, 70, size=len(subs))

fake_age_df.to_csv('cropped/labels.csv', index=False)


