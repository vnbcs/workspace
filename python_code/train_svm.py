from joblib import dump, load
from sklearn.svm import SVR 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

X = load('../files/fingerprintX_pca.joblib') 
y = load('../files/fingerprintY.joblib') 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
print("splitting train and test set...")

model = SVR(kernel='linear', C=100, gamma="auto", verbose=1) # verbose prints training updates 
print("training model...")
model.fit(X_train, y_train)
print("training complete...")

dump(model, '../files/fingerprint_model.joblib')

# print("cross validating...")
# 5 fold cross validation
# scores = cross_validate(model, X, y, cv=5,
#                         scoring=('r2', 'neg_mean_squared_error'),
#                         return_train_score=True)

# dump(scores, '../files/fingerprint_cv_scores.joblib')
print("complete!")