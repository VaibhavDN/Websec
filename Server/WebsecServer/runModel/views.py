from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from importlib.machinery import SourceFileLoader
import datetime

def getLink(request):
    if 'last_connection' in request.COOKIES and 'username' in request.COOKIES:
        print("Cookie Yay!!")
        last_connection = request.COOKIES['last_connection']
        print("COOKIE datetime: "+last_connection)
        last_connection = last_connection.split(' ')
        cookie_date = last_connection[0].split('-')
        current_datetime = str(datetime.datetime.now())
        print("Current datetime: "+current_datetime)
        current_date = current_datetime.split(' ')[0].split('-')
        if(cookie_date[2] == current_date[2]):
            cookie_time = last_connection[1].split('.')[0].split(':')[1]
            current_time = current_datetime.split(' ')[1].split('.')[0].split(':')[1]
            if(abs(int(current_time) - int(cookie_time)) > 10):
                return HttpResponseRedirect("http://127.0.0.1:8000/login/")
        #return HttpResponseRedirect("https://www.google.com")
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/login/")
    pathToModels = os.path.abspath('./')
    pathToModels = pathToModels.split('/')
    pathToModels.pop()
    pathToModels.pop()
    pathToModels.append('Models')
    pathToModels = '/'.join(pathToModels)

    if 'link' in request.GET:
        link = request.GET['link']
    else:
        print("Link not found")
    
    testSitesPath = pathToModels + '/' + "TestSites.txt" 
    fobject = open(testSitesPath, "w")
    fobject.write(link)
    fobject.close()
    pathToParser = pathToModels + '/' + "HTMLParser.py"
    print(pathToModels)
    parser = SourceFileLoader('ParserModule', pathToParser).load_module()
    print(parser)
    prediction1,prediction2 = parser.startParser(pathToModels, 3)
    
    if(prediction1 == 1):
        returnResponse = "<center><H4>Sorry, gaming sites are blocked: "+link+"</H4></center>"
    elif(prediction2 == 2):
        returnResponse = "<center><H4>Sorry, shopping sites are blocked: "+link+"</H4></center>"
    else:
        return HttpResponseRedirect(link)
    return HttpResponse(returnResponse)

