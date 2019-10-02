from sklearn.externals import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def runModel(pathToModels):
    try:
        data = pd.read_csv(pathToModels + '/' + "TestDataset.csv")
        X = data.iloc[:, 1:30]
        #X = X.drop(["card","account"], axis=1)
        model = joblib.load(pathToModels + '/' + "Payment/Payment_Model_XGBoost.pkl")
        prediction = model.predict(X)
        print(prediction)
        return prediction
    except Exception as e:
        print("Exception while classifying: "+str(e))
        prediction = 0
#runModel()
