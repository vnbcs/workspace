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
X_impulse = load('../files/fingerprintX_impulse.joblib') 
y_impulse = load('../files/fingerprinty_impulse.joblib') 

print("splitting train and test sets...")
X_train_impulse, X_test_impulse, y_train_impulse, y_test_impulse = train_test_split(
    X_impulse, y_impulse, test_size = 1/3, random_state = 0)

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

print("fitting data...")
impulse_gs = GridSearchCV(pipe, all_params, cv = 3, scoring=scorer, verbose=1)
impulse_gs.fit(X_train_impulse,y_train_impulse)

dump(impulse_gs, '../files/fingerprint_impulse_gs_r2.joblib')