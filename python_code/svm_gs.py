from joblib import dump, load
from sklearn.svm import SVR 
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import GridSearchCV

X = load('../files/fingerprintX_pca.joblib') 
y = load('../files/fingerprintY.joblib') 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
scorer = make_scorer(mean_squared_error, greater_is_better=False)

# SVR
svr_parameters = [
    {"kernel": ["linear"], "gamma": [1e-2,1e-3,1e-4,"auto"], "C": [1, 10, 100, 1000]},
]

svr_gs = GridSearchCV(SVR(verbose = 1), svr_parameters, cv = 10, scoring=scorer, verbose=1)
svr_gs.fit(X_train,y_train)

dump(svr_gs, '../files/fingerprint_svr_gs.joblib')

# SVR
print("fitting SVR...")
svr_parameters = [
    {"kernel": ["linear"], "gamma": [1e-2,1e-3,1e-4,"auto"], "C": [1, 10, 100, 1000]},
]

svr_gs = GridSearchCV(SVR(verbose = 1), svr_parameters, cv = 10, scoring=scorer, verbose=1)
svr_gs.fit(X_train,y_train)

dump(svr_gs, '../files/fingerprint_svr_gs.joblib')

# Ridge
print("fitting Ridge...")
ridge_parameters = [
    {"alpha": [np.logspace(-4, 4, 5)], "random_state": [0], "solver": ["auto","lsqr","saga"]},
]

ridge_gs = GridSearchCV(Ridge(verbose = 1), ridge_parameters, cv = 10, scoring=scorer, verbose=1)
ridge_gs.fit(X_train,y_train)

dump(ridge_gs, '../files/fingerprint_ridge_gs.joblib')

# Lasso
print("fitting Lasso...")
lasso_parameters = [
    {"alpha": [np.logspace(-4, 4, 5)], "random_state": [0], "selection": ["cyclic","random"]},
]

lasso_gs = GridSearchCV(Lasso(verbose = 1), lasso_parameters, cv = 10, scoring=scorer, verbose=1)
lasso_gs.fit(X_train,y_train)

dump(lasso_gs, '../files/fingerprint_lasso_gs.joblib')