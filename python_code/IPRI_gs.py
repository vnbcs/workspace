print("importing packages...")
from joblib import dump, load
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
#from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

print("loading data...")
X_pca = load('../files/fingerprintX_pca.joblib')
y_29 = load('../files/fingerprinty_29.joblib')
y_30 = load('../files/fingerprinty_30.joblib') 
y_31 = load('../files/fingerprinty_31.joblib') 
y_32 = load('../files/fingerprinty_32.joblib') 

print("splitting train and test sets...")
X_train29, X_test29, y_train29, y_test29 = train_test_split(
  X_pca, y_29, test_size = 1/3, random_state = 0)
  
X_train30, X_test30, y_train30, y_test30 = train_test_split(
  X_pca, y_30, test_size = 1/3, random_state = 0)
  
X_train31, X_test31, y_train31, y_test31 = train_test_split(
  X_pca, y_31, test_size = 1/3, random_state = 0)
  
X_train32, X_test32, y_train32, y_test32 = train_test_split(
  X_pca, y_32, test_size = 1/3, random_state = 0)

print("preparing pipeline...")
#scorer = make_scorer(mean_squared_error, greater_is_better=False)
scorer = make_scorer(r2_score)

svr = SVR()
ridge = Ridge(random_state=0)
#lasso = Lasso()
en = ElasticNet(random_state=0)
gbr = GradientBoostingRegressor(random_state=0)
pipe = Pipeline([('model',svr)])

all_params = [
    {'model' : [svr], 'model__kernel' : ['linear'],
    "model__gamma" : [1e-2,1e-3,"auto"], "model__C" : np.logspace(-2, 2, 3)
    },
    {'model' : [ridge], 'model__alpha' : np.logspace(-2, 2, 3), 'model__solver' : ['lsqr','saga']
    },
#     {'model' : [lasso], 'model__alpha' : np.logspace(-2, 2, 3),
#     'model__random_state' : [0], 'model__selection' : ['cyclic','random']
#     },
    {'model' : [en], 'model__alpha' : np.logspace(-2, 2, 3),
    'model__l1_ratio' : np.logspace(-2, 0, 3),
    'model__selection' : ['cyclic','random']
    }
   ,
    {'model' : [gbr], 'model__learning_rate' : np.logspace(-3, -1, 3),
    'model__n_estimators' : [int(x) for x in np.logspace(1,3,3)],
    'model__n_iter_no_change': [50], 'model__max_depth': [2,4,6]
    }

]

print("fitting IPRI_29...")
gs_29 = GridSearchCV(pipe, all_params, cv = 3, scoring=scorer, verbose=1)
gs_29.fit(X_train29,y_train29)

dump(gs_29, '../files/fingerprint_29_gs_r2.joblib')
print("\n\n\n\n---------------------------\n")

print("fitting IPRI_30...")
gs_30 = GridSearchCV(pipe, all_params, cv = 3, scoring=scorer, verbose=1)
gs_30.fit(X_train30,y_train30)

dump(gs_30, '../files/fingerprint_30_gs_r2.joblib')
print("\n\n\n\n---------------------------\n")

print("fitting IPRI_31...")
gs_31 = GridSearchCV(pipe, all_params, cv = 3, scoring=scorer, verbose=1)
gs_31.fit(X_train31,y_train31)

dump(gs_31, '../files/fingerprint_31_gs_r2.joblib')
print("\n\n\n\n---------------------------\n")

print("fitting IPRI_32...")
gs_32 = GridSearchCV(pipe, all_params, cv = 3, scoring=scorer, verbose=1)
gs_32.fit(X_train32,y_train32)

dump(gs_32, '../files/fingerprint_32_gs_r2.joblib')