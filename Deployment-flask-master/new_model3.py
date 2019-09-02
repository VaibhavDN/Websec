#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import pickle


# In[4]:


data=pd.read_csv('C:/Users/Anubhav Sanyal/Desktop/Minor Project/output_final.csv')


# In[5]:


data


# In[6]:


X=data.iloc[:,0]


# In[7]:


y=data.iloc[:,1]


# In[8]:


for i in range(0,58):
    X[i]=X[i].lower()


# In[9]:


X


# In[10]:


y=data.iloc[:,1]


# In[11]:


from sklearn.feature_extraction.text import CountVectorizer


# In[12]:


cv=CountVectorizer(max_features=7000)


# In[13]:


X_vec=cv.fit_transform(X)


# In[14]:


X_vec


# In[15]:


X_vec.shape


# In[16]:


from sklearn.feature_extraction.text import TfidfTransformer


# In[17]:


tf=TfidfTransformer()


# In[18]:


X_tf=tf.fit_transform(X_vec)


# In[19]:


X_tf


# In[20]:


X_tf.shape


# In[21]:


from sklearn.linear_model import LogisticRegression


# In[22]:


lr=LogisticRegression()


# In[23]:


lr.fit(X_tf,y)


# In[24]:


pickle.dump(lr,open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','wb'))


# In[26]:


model3 = pickle.load(open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','rb'))


# In[ ]:




