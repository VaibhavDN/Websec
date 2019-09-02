import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
def load_model(a):
    #!/usr/bin/env python
# coding: utf-8

# In[3]:


    import numpy as np


# In[4]:


    import pandas as pd


# In[5]:


    import pickle


# In[6]:


    data=pd.read_csv('C:/Users/Anubhav Sanyal/Desktop/Minor Project/output_final.csv')


# In[7]:





# In[8]:


    X=data.iloc[:,0]


# In[9]:


    y=data.iloc[:,1]


# In[10]:


    for i in range(0,58):
        X[i]=X[i].lower()


# In[11]:





# In[12]:


    y=data.iloc[:,1]


# In[13]:


    from sklearn.feature_extraction.text import CountVectorizer


# In[14]:


    cv=CountVectorizer(max_features=7000)


# In[15]:


    X_vec=cv.fit_transform(X)


# In[16]:





# In[17]:




# In[18]:


    from sklearn.feature_extraction.text import TfidfTransformer


# In[19]:


    tf=TfidfTransformer()


# In[20]:


    X_tf=tf.fit_transform(X_vec)


# In[21]:



# In[22]:




# In[23]:


    from sklearn.linear_model import LogisticRegression


# In[24]:


    lr=LogisticRegression()


# In[25]:


    lr.fit(X_tf,y)


# In[24]:


#pickle.dump(lr,open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','wb'))


# In[26]:


#model3 = pickle.load(open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','rb'))


# In[26]:




# In[27]:

    a=str(a)
    a=[a]


# In[29]:


    a=cv.transform(a)


# In[30]:


    a=tf.transform(a)


# In[31]:


    u=lr.predict(a)
    print(u)
    return u


# In[ ]:





@app.route('/predict',methods=['POST'])
def predict():
    #'''
     #For rendering results on HTML GUI
    #'''
    a=str(input('enter the scraped text'))
    a=[a]
    ##a = request.form.values()
        #!/usr/bin/env python
# coding: utf-8

# In[3]:


    import numpy as np


# In[4]:


    import pandas as pd


# In[5]:


    import pickle


# In[6]:


    data=pd.read_csv('C:/Users/Anubhav Sanyal/Desktop/Minor Project/output_final.csv')


# In[7]:





# In[8]:


    X=data.iloc[:,0]


# In[9]:


    y=data.iloc[:,1]


# In[10]:


    for i in range(0,58):
        X[i]=X[i].lower()


# In[11]:





# In[12]:


    y=data.iloc[:,1]


# In[13]:


    from sklearn.feature_extraction.text import CountVectorizer


# In[14]:


    cv=CountVectorizer(max_features=7000)


# In[15]:


    X_vec=cv.fit_transform(X)


# In[16]:





# In[17]:




# In[18]:


    from sklearn.feature_extraction.text import TfidfTransformer


# In[19]:


    tf=TfidfTransformer()


# In[20]:


    X_tf=tf.fit_transform(X_vec)


# In[21]:



# In[22]:




# In[23]:


    from sklearn.linear_model import LogisticRegression


# In[24]:


    lr=LogisticRegression()


# In[25]:


    lr.fit(X_tf,y)


# In[24]:


#pickle.dump(lr,open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','wb'))


# In[26]:


#model3 = pickle.load(open('C:/Users/Anubhav Sanyal/Desktop/Minor Project/new_model3.pkl','rb'))


# In[26]:




# In[27]:

    


# In[29]:


    a=cv.transform(a)


# In[30]:


    a=tf.transform(a)


# In[31]:


    u=lr.predict(a)
    


# In[ ]:




    #final_features = [np.array(int_features)] 
    #prediction = model.predict(final_features)
    if(u==1):

        u='Tech Blogs'
    elif(u==2):
        u='Entertainment(Bollywood/Hollywood)Blog'
    elif(u==3):
        u='Porn/Adult Website'


    return render_template('index.html', prediction_text='The site should be blocked as it falls in Category of {}'.format(u))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
