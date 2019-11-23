from sklearn.externals import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def runModel(pathToModels):

    try:
        data = pd.read_csv(pathToModels + '/' + "TestDataset.csv")
        X = data.iloc[:, 1:30]
        X = X.drop(['product','top','set','best','please','detail'], axis=1)
        #Y = data.iloc[:, -1]
        
        model = joblib.load(pathToModels + '/' + "Shopping/Shopping_Model_XGBoost.pkl")
        prediction = model.predict(X)
        
    except Exception as e:
        print("Exception while classifying: "+str(e))
        prediction = 0

    print(prediction)
    return prediction
    #print(accuracy_score(prediction, Y, normalize=True))
#runModel()
