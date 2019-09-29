from sklearn.externals import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def runModel():
    data = pd.read_csv("TestDataset.csv")

    X = data.iloc[:, 1:30]
    X = X.drop(["free","download"], axis=1)
    #Y = data.iloc[:, -1]
    
    model = joblib.load("Gaming_Model_XGBoost.pkl")
    prediction = model.predict(X)

    print(prediction)
    #print(accuracy_score(prediction, Y, normalize=True))
runModel()
