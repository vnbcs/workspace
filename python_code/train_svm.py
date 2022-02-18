from joblib import dump, load
from sklearn.svm import SVC 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

X = load('../files/fingerprintX.joblib') 
y = load('../files/fingerprintY.joblib') 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

model = SVC(kernel='linear', C=1E5, verbose=True) # verbose prints training updates 
model.fit(X_train, y_train)

dump(model, '../files/fingerprint_model.joblib')

# 5 fold cross validation
scores = cross_val_score(model, X, y, cv=5)
dump(scores, '../files/fingerprint_cv_scores.joblib')