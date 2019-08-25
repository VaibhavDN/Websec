import collections
from nltk.corpus import stopwords
import os

for filename in os.listdir('C:\\mv_db'):
    file = open('C:\Movie_site_scraper\mv_db\\' + filename, 'r')
    str_list = file.readlines()
    token_list = []
    for j in str_list:
        j = j[0:len(j)-1]
        buff_list = j.split(' ')
        token_list+=buff_list
        
    for i in token_list:
        if not i.isalnum() or len(i)== 1:
            del token_list[token_list.index(i)]
            
    filtered_tk = [word for word in token_list if word not in stopwords.words('english')]
    token_f  = collections.Counter(filtered_tk)
    
    file_1 = open('C:\Movie_site_scraper\mv_db_keywords\\' + filename, 'w')
    for i in filtered_tk:
        file_1.write(i)
        file_1.write('\n')
    
