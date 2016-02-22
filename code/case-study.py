from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

df = pd.read_csv('data/churn.csv')
df['last_trip_date'] = pd.to_datetime(df['last_trip_date'])
df['signup_date'] = pd.to_datetime(df['signup_date'])
dummies = pd.get_dummies(df['city'])
df['Astapor'] = dummies['Astapor']
df["King's Landing"] = dummies["King's Landing"]
df['Winterfell'] = dummies['Winterfell']
df[['Android', 'iPhone']] = pd.get_dummies(df['phone'])
print 'hi'

# Created Churn Column / target variable

df['Churn'] = df['last_trip_date'] < pd.to_datetime('2014-06-01')


# filled in missing values for ratings and phone type

df['avg_rating_of_driver'].fillna(value=4.900000, inplace=True)
df['avg_rating_by_driver'].fillna(value=5.000000, inplace=True)
df['phone'].fillna(value='iPhone', inplace=True)

temp = pd.to_datetime('2014-07-01') - df['last_trip_date']
df['days_since_last_trip'] = (temp / np.timedelta64(1, 'D')).astype(int)

print 'hi'
temp = pd.to_datetime('2014-07-01') - df['signup_date']
df['days_since_signup'] = (temp / np.timedelta64(1, 'D')).astype(int)

y = df['Churn']
X = df.drop(['city', 'phone', 'signup_date', 'last_trip_date', 'Churn', 'days_since_last_trip', 'days_since_signup'], axis=1)

# param_grid_logistic = [
#   {'C': [0.1, 1, 10, 100], 'penalty': ['l1', 'l2']}
#  ]

# param_grid_svc = [
#   {'C': list(np.linspace(1, 30, 3)), 'kernel': ['linear']},
#   {'C': list(np.linspace(1, 30, 3)), 'gamma': [0.001, 0.01, 0.1, 1], 'kernel': ['rbf']},
#   {'C': list(np.linspace(1, 30, 3)), 'degree': [2, 3, 4], 'kernel': ['poly']}
#  ]

#  param_grid_svc = [
#   {'C': list(np.linspace(1, 30, 3)), 'kernel': ['linear']},
#   {'C': list(np.linspace(1, 30, 3)), 'gamma': [0.001, 0.01, 0.1, 1], 'kernel': ['rbf']},
#   {'C': list(np.linspace(1, 30, 3)), 'degree': [2, 3, 4], 'kernel': ['poly']}]

param_grid_gbc = [{'learning_rate': list(np.linspace(0.001, 1, 4)), 'n_estimators': [10, 50, 100], 'max_depth': [1, 3, 6], 'max_features': ['auto', 'sqrt', 'log2']}
 ]
print 'hi'

# lg = LogisticRegression()

# gs_log = GridSearchCV(lg, param_grid_logistic, scoring='accuracy', cv=5)
# gs_log.fit(X.values, y)
# print gs_log.best_params_
# print gs_log.

svm = SVC()

gbc = GradientBoostingClassifier()

model = GridSearchCV(gbc, param_grid_gbc, scoring='accuracy', cv=3)
model.fit(X.values, y)
print model.best_params_
print model.best_score_
print 'hi'
