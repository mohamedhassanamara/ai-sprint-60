from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score

import pandas as pd
import joblib

class ChurnPredictor:
    def __init__(self):
        self.model = RandomForestClassifier()


df = pd.read_csv('telco_churn.csv')
df_encoded = pd.get_dummies(df, columns=['contract_type'], dtype=int)

print(df_encoded.to_string())
x,y = df_encoded.drop('churn', axis=1), df_encoded['churn']
predictor = ChurnPredictor()
x_train,x_test, y_train,  y_test = train_test_split(x, y, test_size=0.2)
predictor.model.fit(x_train, y_train)
print(predictor.model.score(x_test, y_test))
print(accuracy_score(y_test, predictor.model.predict(x_test)))
print(recall_score(y_test, predictor.model.predict(x_test)))
print(precision_score(y_test, predictor.model.predict(x_test)))
joblib.dump(predictor.model, 'rf_churn_model.joblib')
