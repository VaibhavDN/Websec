import requests
from bs4 import BeautifulSoup

try:
    html=requests.get('https://stackexchange.com').text
    soup = BeautifulSoup(html, 'lxml')
    bodyContent = soup.body
      # Remove all script and style elements
    for script in bodyContent(["script", "style"]):
        script.decompose()
    bodyContentTxt = bodyContent.get_text()
    bodyContentStr = str(bodyContentTxt)
    #bodyWithoutSpaces = bodyContentStr.replace(" ","")
    bodyWithoutSpaces = bodyContentStr.replace("\n","")
    bodyContentLength = len(bodyWithoutSpaces)
    print(bodyWithoutSpaces)
    print(bodyContentLength)
except Exception as e:
    print("Exception: " + str(e))
fobject=open("Stack_exchange.txt","w")
for words in bodyWithoutSpaces:
    try:
        fobject.write(words)
    except:
        print("skip")    


fobject.close()
