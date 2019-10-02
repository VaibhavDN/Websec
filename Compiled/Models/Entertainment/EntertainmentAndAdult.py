def predict(pathToModels):
    import numpy as np
    import pandas as pd
    import pickle
    data=pd.read_csv(pathToModels+'/EntertainmentAndAdult/output_final.csv')


    # In[7]:


    data


    # In[8]:


    X=data.iloc[:,0]


    # In[9]:


    y=data.iloc[:,1]


    # In[10]:


    for i in range(0,58):
        X[i]=X[i].lower()


    # In[11]:


    X


    # In[12]:


    y=data.iloc[:,1]


    # In[13]:


    from sklearn.feature_extraction.text import CountVectorizer


    # In[14]:


    cv=CountVectorizer(max_features=7000)


    # In[15]:


    X_vec=cv.fit_transform(X)


    # In[16]:


    X_vec


    # In[17]:


    X_vec.shape


    # In[18]:


    from sklearn.feature_extraction.text import TfidfTransformer


    # In[19]:


    tf=TfidfTransformer()


    # In[20]:


    X_tf=tf.fit_transform(X_vec)


    # In[21]:


    X_tf


    # In[22]:


    X_tf.shape


    # In[23]:


    from sklearn.linear_model import LogisticRegression


    # In[24]:


    lr=LogisticRegression()


    # In[25]:


    lr.fit(X_tf,y)


    # In[24]:


    pickle.dump(lr,open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','wb'))


    # In[26]:


    model3 = pickle.load(open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','rb'))


    # In[26]:


    a=str(input("enter the text"))


    # In[27]:


    a=[a]


    # In[29]:


    a=cv.transform(a)


    # In[30]:


    a=tf.transform(a)


    # In[31]:


    u=lr.predict(a)
    print(u)


    # In[ ]:




