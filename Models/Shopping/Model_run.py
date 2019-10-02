from sklearn.externals import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def runModel():
    data = pd.read_csv("TestDataset.csv")
    
    X = data.iloc[:, 1:30]
    #X = X.drop(['product','top','set','best','please','policy','privacy','term','login','right','phone','full','enter','le','password','cancel','payment','english','app','register','hindi','copy','every','helpful','city','game','detail','great'], axis=1)
    X = X.drop(['product','top','set','best','please','detail'], axis=1)
    #Y = data.iloc[:, -1]

    model = joblib.load("Shopping_Model_XGBoost.pkl")
    prediction = model.predict(X)

    print(prediction)
    #print(accuracy_score(prediction, Y, normalize=True))
runModel()
