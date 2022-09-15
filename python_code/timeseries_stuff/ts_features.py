# to use
# python ts_features.py /path/to/timeseries.txt /path/and/name/of/desired/output_file.tsv
# python ts_features.py extracted_timeseries-3.txt timeseries_features.tsv

import numpy as np
import pandas as pd
from scipy import stats
from pyentrp import entropy as ent
import sys

ts_file, out_path = sys.argv[1:3]

ts = np.genfromtxt(ts_file)
ts_z = stats.zscore(ts, axis=0)

kurt = stats.moment(ts_z, 4, axis=0) / np.std(ts_z, axis=0)
sd = np.std(ts, axis=0)
tsnr = np.mean(ts, axis=0) / sd

succ_diffs = ts[1:] - ts[:-1]
mssd = np.sum(succ_diffs**2, axis=0) / succ_diffs.shape[0]

se = []
lag1 = []
for i in range(len(ts.T)):
    se.append(ent.sample_entropy(ts_z[:,i], 3, tolerance=0.5)[-1])
    lag1.append(np.corrcoef(ts_z[1:,i],ts_z[:-1,i])[0,1])
se = np.array(se)
lag1 = np.array(lag1)

out_df = pd.DataFrame(np.array([kurt, sd, tsnr, mssd, lag1, se]).T,
columns=['kurtosis','SD','tSNR','MSSD','Lag1','sample_entropy'])

out_df.to_csv(out_path, sep='\t')
