from bs4 import BeautifulSoup
import requests



def cral(resp, file_n, count):
    bs_ob = BeautifulSoup(resp.text, features='html.parser')
    f_arr = []
    file_nm = file_n.split('/')[2]
    print(file_nm)
    tag_find = ['a','button','option','title','div']
    a_tag = bs_ob.find_all(tag_find)
    for link in a_tag:
        tx_1 = link.string
        if tx_1 != None:
            f_arr.append(tx_1.strip())
    
    if len(f_arr) > 8:
        file = open('C:\Movie_site_scraper\mv_db\\' + file_nm + '.txt' ,'w')
        for i in f_arr:
            file.write(i)
            file.write('\n')
        file.close()
        count+=1
    
            
    return count


count = 0
file = open('C:\Movie_site_scraper\mvdb.txt','r')
web_st = file.readlines()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
web_st = list(dict.fromkeys(web_st))

print('Total links',len(web_st))

for i in web_st:
    try:
        file_nm = i.split('/')[2]
        file_ch = open('C:\Movie_site_scraper\mv_db\\' + file_nm + '.txt' ,'r')
        file_ch.close()
        print(i,'visited')
    except:
        try:
            resp = requests.get(i, headers=headers)
            print(i+'Success')
            count = cral(resp, i, count)
        except:
            print('Error')
            del web_st[web_st.index(i)]
        

print(count,'files written')
file.close()
file = open('C:\Movie_site_scraper\mvdb.txt','w')
file.writelines(web_st)
file.close()


    
