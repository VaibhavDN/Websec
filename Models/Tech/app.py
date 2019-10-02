def predict(pathToModels,pageParsedContent):
    import numpy as np
    import pandas as pd
    import requests
    import matplotlib.pyplot as plt
    from bs4 import BeautifulSoup
    data=pd.read_csv(pathToModels+'/Tech/odf_scraped.csv')
    X=data.iloc[:,0]
    y=data.iloc[:,1]
    from sklearn.feature_extraction.text import CountVectorizer
    cv=CountVectorizer(max_features=200)
    X_vec=cv.fit_transform(X)
    from sklearn.feature_extraction.text import TfidfTransformer
    tf=TfidfTransformer()
    X_tf=tf.fit_transform(X_vec)
    from sklearn.linear_model import LogisticRegression
    lr=LogisticRegression()
    lr.fit(X_tf,y)
    print('done successfuly till here')
    soup=pageParsedContent
    main_title=soup.find('title')
    main_title=main_title.get_text()
    main_title=main_title.replace(","," ")
    with open(pathToModels+'/Tech/final_testing.txt','w') as f:
        f.write(main_title+'\n')
        f.close()
    with open(pathToModels+'/Tech/final_testing.txt','r') as f:
        text_test=f.read()
        f.close()
    text_test=[text_test]
    text_test_cv=cv.transform(text_test)
    text_test_tf=tf.transform(text_test_cv)
    u=lr.predict(text_test_tf)
    print(u)
    
    if(u==1):
        return u
    

    #output = round(prediction[0], 2)
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    sw=set(stopwords.words('english'))
    num=[]
    for i in range(0,3000):
        i=str(i)
        num.append(i)
    mx=['(',')',',','.','?','#','@','!','[',']','<','>','/',' ','|',"''",'...',':']
    soup=pageParsedContent
    body_content=soup.body
    for script in body_content(["script", "style"]):
        script.decompose()
    body_content_text=body_content.get_text()
    body_content_text=body_content_text.replace('\n',' ')
    body_content_text=body_content_text.replace('\t',' ')
    body_content_text=body_content_text.replace("'",' ')
    with open(pathToModels+'/Tech/final_scraped_content_test.txt','w') as f:
        f.write(body_content_text)
        f.close()
    with open(pathToModels+'/Tech/final_scraped_content_test.txt','r') as f:
        new_text=f.read()
        f.close()
    from nltk.tokenize import sent_tokenize
    sent=sent_tokenize(new_text)
    data=[]
    for i in sent:
        words=word_tokenize(i)
        for w in words:
            if w not in sw and w not in mx and w not in num:
                data.append(w)
    from collections import Counter
    count=Counter(data)
    count=sorted(count.items(), key=lambda x: x[1], reverse=True)
    tech=['Samsung','Xiaomi','Lenovo','Vivo','Oppo','Apple','LG','Nokia','OnePlus','HTC','Huawei','Amazon','Flipkart','Google','Mobile','Smartphones','Smartphone','Laptop','AI','Robots','Gaming','Headphone','PC','Computers','Apps','App','Phones','Phone','Smart','Android','iOS','Snapdragon','Qualcom','Intel','Startups','Startups','smartwatch','Realme','Redmi','Bluetooth','Camera']
    cc=0
    ff=0
    for i in range(0,len(count)-1):
        de=count[i][1]
        if(de==1):
            ff=ff+1
        else:
            cc=cc+de
    score=0
    b=0
    t=0
    for i in range(0,len(count)-1):
        a=count[i][0]
        b=count[i][1]
        for k in tech:
            if(a==k):
                print(a)
                b=b/cc
                t=t+b
            
                print(b)
                score=score+1
    fp=count[0][1]
    xy=fp/cc
    if(b>xy and score>7):
        return 1
    else:
        return 0

