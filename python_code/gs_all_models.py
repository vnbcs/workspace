print("importing packages...")
from joblib import dump, load
import numpy as np
from sklearn.svm import SVR
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import GridSearchCV

print("loading data...")
X = load('../files/fingerprintX_pca.joblib')
y = load('../files/fingerprintY.joblib')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
scorer = make_scorer(mean_squared_error, greater_is_better=False)

svr = SVR()
ridge = Ridge()
lasso = Lasso()
en = ElasticNet()
gbr = GradientBoostingRegressor()
pipe = Pipeline([('model',svr)])

all_params = [
#     {'model' : [svr], 'model__kernel' : ['linear'],
#     "model__gamma" : [1e-2,1e-3,1e-4,"auto"], "model__C" : np.logspace(-4, 4, 5)
#     },
#     {'model' : [ridge], 'model__alpha' : np.logspace(-4, 4, 5),
#     'model__random_state' : [0], 'model__solver' : ['auto','lsqr','saga']
#     },
#     {'model' : [lasso], 'model__alpha' : np.logspace(-4, 4, 5),
#     'model__random_state' : [0], 'model__selection' : ['cyclic','random']
#     },
#     {'model' : [en], 'model__alpha' : np.logspace(-4, 4, 5),
#     'model__random_state' : [0], 'model__l1_ratio' : np.logspace(-4, 0, 5),
#     'model__selection' : ['cyclic','random']
#     }
#    ,
    {'model' : [gbr], 'model__learning_rate' : np.logspace(-3, -1, 3),
    'model__random_state' : [0], 'model__n_estimators' : [int(x) for x in np.logspace(1,3,3)],
    'model__n_iter_no_change': [50], 'model__max_depth': [2,4,6,8]
    }

]

print("fitting models...")
all_gs = GridSearchCV(pipe, all_params, cv = 2, scoring=scorer, verbose=1)
all_gs.fit(X_train,y_train)

dump(all_gs, '../files/fingerprint_all_gs.joblib')
