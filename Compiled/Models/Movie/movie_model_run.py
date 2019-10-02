import os
from nltk.corpus import stopwords
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as nt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm, linear_model
from sklearn.metrics import accuracy_score
import pickle

def model(tk1, tk2, data_m):
    nb = linear_model.LogisticRegression(random_state=0, solver='lbfgs',multi_class='multinomial')
    nb.fit(tk1 ,data_m['Category'])
    pred = nb.predict(tk2)
    print(pred)
    return pred
    

def tknz(pathToModels,data_st):
    data_s = pd.DataFrame(data_st)

    data_m = pd.read_csv(pathToModels+'/Movie/movie_t.csv', encoding = 'utf-8')
    s = data_m['text_final']

    nt_arr = defaultdict(lambda : nt.NOUN)
    nt_arr['J'] = nt.ADJ
    nt_arr['V'] = nt.VERB
    nt_arr['R'] = nt.ADV

    data_s['Text'] = [entry.lower() for entry in data_s['Text']]
    data_s['Text']= [word_tokenize(entry) for entry in data_s['Text']]

    for index,entry in enumerate(data_s['Text']):
        proc_arr = []
        word_Lemmatized = WordNetLemmatizer()
        for word, tag in pos_tag(entry):
            if word not in stopwords.words('english') and word.isalpha():
                word_Final = word_Lemmatized.lemmatize(word,nt_arr[tag[0]])
                proc_arr.append(word_Final)
        s.loc[72] = str(proc_arr)

    print(s[72])

    Tf = TfidfVectorizer(max_features=5000)
    Tf.fit(data_m['text_final'][0:72])
    Train_X_tf = Tf.transform(data_m['text_final'][0:72])
    Test_X_tf = Tf.transform([s[72]])
    pred = model(Train_X_tf, Test_X_tf, data_m)
    return pred
    

def cral(pathToModels,bs_ob):
    text = bs_ob
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    dict = {'Text':[]}
    dict['Text'].append(text)
    return tknz(pathToModels,dict)

def fetch(url):
    brs = webdriver.Firefox()
    brs.get(url)
    resp = brs.page_source
    cral(resp)

#fetch()
