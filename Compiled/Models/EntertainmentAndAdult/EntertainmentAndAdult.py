def predict(pathToModels,bodyContentWithoutTags):
    import numpy as np
    import pandas as pd
    import pickle
    data=pd.read_csv(pathToModels+'/EntertainmentAndAdult/output_final.csv')
    X=data.iloc[:,0]
    y=data.iloc[:,1]
    for i in range(0,58):
        X[i]=X[i].lower()
    y=data.iloc[:,1]

    from sklearn.feature_extraction.text import CountVectorizer

    cv=CountVectorizer(max_features=7000)

    X_vec=cv.fit_transform(X)

    X_vec.shape

    from sklearn.feature_extraction.text import TfidfTransformer

    tf=TfidfTransformer()
    X_tf=tf.fit_transform(X_vec)
    X_tf
    X_tf.shape

    from sklearn.linear_model import LogisticRegression
    lr=LogisticRegression()
    lr.fit(X_tf,y)
    pickle.dump(lr,open(pathToModels+'/EntertainmentAndAdult/EntAndAdlt.pkl','wb'))
    model3 = pickle.load(open(pathToModels+'/EntertainmentAndAdult/EntAndAdlt.pkl','rb'))
    a=bodyContentWithoutTags
    a=[a]
    a=cv.transform(a)
    a=tf.transform(a)
    u=lr.predict(a)
    print(u)
    return u