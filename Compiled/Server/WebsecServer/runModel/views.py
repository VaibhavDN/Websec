from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from importlib.machinery import SourceFileLoader
import datetime
from Login.models import Logs

def getLink(request):
    username = ""
    if 'last_connection' in request.COOKIES and 'username' in request.COOKIES:
        print("Cookie Yay!!")
        username = request.COOKIES['username']
        last_connection = request.COOKIES['last_connection']
        print("COOKIE datetime: "+last_connection)
        last_connection = last_connection.split(' ')
        cookie_date = last_connection[0].split('-')
        current_datetime = str(datetime.datetime.now())
        print("Current datetime: "+current_datetime)
        current_date = current_datetime.split(' ')[0].split('-')
        if(cookie_date[2] == current_date[2]):
            cookie_time = last_connection[1].split('.')[0].split(':')[1]
            current_time = current_datetime.split(
                ' ')[1].split('.')[0].split(':')[1]
            if(abs(int(current_time) - int(cookie_time)) > 10):
                return HttpResponseRedirect("http://0.0.0.0:4000/login/")
        # return HttpResponseRedirect("https://www.google.com")
    else:
        return HttpResponseRedirect("http://0.0.0.0:4000/login/")
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

    prediction1=0
    prediction2=0
    prediction3=0
    prediction4=1
    prediction5=1
    prediction6=0
    prediction7=0

    if(os.path.isfile(pathToModels + "/locked_helper.txt") and os.path.isfile(pathToModels + "/locked.txt")):
        counter = 0
        while(os.path.isfile(pathToModels + "/locked.txt") and counter < 1000000):
            print("Waiting.. Current url: "+link)
            counter+=1
        if(counter >= 1000000):
            try:
                os.remove(pathToModels + "/locked.txt")
            except Exception as e:
                print(e)


    if(not os.path.isfile(pathToModels + "/locked.txt")):
        fobject = open(pathToModels + "/locked.txt", "w")
        fobject.write(link)
        fobject.close()

        testSitesPath = pathToModels + '/' + "TestSites.txt"
        fobject = open(testSitesPath, "w")
        fobject.write(link)
        fobject.close()
        pathToParser = pathToModels + '/' + "HTMLParser.py"
        print(pathToModels)
        parser = SourceFileLoader('ParserModule', pathToParser).load_module()
        print(parser)

        prediction1, prediction2, prediction3, prediction4, prediction5, prediction6, prediction7 = parser.startParser(
            pathToModels, 3, request.COOKIES['username'])
        try:
            os.remove(pathToModels + "/locked.txt")
        except Exception as e:
            print(e)

    else:   #elif(not os.path.isfile(pathToModels + "/locked_helper.txt"))
        fobject = open(pathToModels + "/locked_helper.txt", "w")
        fobject.write(link)
        fobject.close()
        helper = SourceFileLoader('HelperModule', os.path.abspath("./") + "/runModel/p2p_client.py").load_module()
        prediction1, prediction2, prediction3, prediction4, prediction5, prediction6, prediction7 = helper.run_helper_server((link+"|"), request.COOKIES['username'])
        try:
            os.remove(pathToModels + "/locked_helper.txt")
        except Exception as e:
            print(e)

    logs = Logs()
    status = "allowed"
    if(prediction1 == 1):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, gaming sites are blocked: "+link+"</H4></center>"
    elif(prediction2 == 1):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, shopping sites are blocked: "+link+"</H4></center>"
    elif(prediction3 == 1):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, payment sites are blocked: "+link+"</H4></center>"
    elif(prediction4 == 0):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, movie sites are blocked: "+link+"</H4></center>"
    elif(prediction5 == 0):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, video streaming sites are blocked: " + \
            link+"</H4></center>"
    elif(prediction6 == 1):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, tech sites are blocked: "+link+"</H4></center>"
    elif(prediction7 > 1):
        status = "blocked"
        returnResponse = "<center><H4>Sorry, entertainment and adult sites are blocked: " + \
            link+"</H4></center>"
    else:
        status = "allowed"
        logs.username = username
        logs.site = link
        logs.status = status
        logs.save()
        return HttpResponseRedirect(link)
        
    logs.username = username
    logs.site = link
    logs.status = status
    logs.save()
    return HttpResponse(returnResponse)
