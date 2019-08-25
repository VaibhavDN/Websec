from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import os
from importlib.machinery import SourceFileLoader

def getLink(request):
    pathToModels = os.path.abspath('./')
    pathToModels = pathToModels.split('/')
    pathToModels.pop()
    pathToModels.pop()
    pathToModels.append('Models')
    pathToModels = '/'.join(pathToModels)

    if 'link' in request.GET:
        link = request.GET['link']
    
    testSitesPath = pathToModels + '/' + "TestSites.txt" 
    fobject = open(testSitesPath, "w")
    fobject.write(link)
    fobject.close()
    pathToParser = pathToModels + '/' + "HTMLParser.py"
    print(pathToModels)
    parser = SourceFileLoader('ParserModule', pathToParser).load_module()
    print(parser)
    prediction = parser.startParser(pathToModels, 3)
    
    if(prediction == 1):
        returnResponse = "<center><H4>Sorry, this site is blocked: "+link+"</H4></center>"
    else:
        return HttpResponseRedirect(link)
    return HttpResponse(returnResponse)

