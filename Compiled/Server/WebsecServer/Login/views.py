from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserDetails, AdminDetails, ModelsActiveStatus, Logs
import datetime
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import StatusSerializer, LogSerializer
from rest_framework.response import Response

#***************************************************************************************

def saveModelSettings(request):
    username = ""
    try:
        username = request.POST["selectUser"]
    except:
        return HttpResponse("<center><h3>Bad request (-_-\")</h3></center>")
    print(request.POST)
    user = ModelsActiveStatus.objects.get(username=username)
    print(user)
    modelsList = ["game", "shopping", "payment", "movie", "video", "tech", "entertainment"]
    newStatusString = ""
    for model in modelsList:
        try:
            if model in request.POST:   #Unchecked checkboxes are not posted using POST by form
                newStatusString+="1"
            else:
                newStatusString+="0"
        except:
            return 1
    print(newStatusString)
    user.statusString = newStatusString
    user.save()
    return 0

#***************************************************************************************

def ShowLoginPage(request):
    if request.POST:
        print(request.POST)
        try:
            username = request.POST['username'] #!To change to if username in request.POST
            loginType = request.POST['loginType']
        except:
            saved = saveModelSettings(request)
            if saved == 0:
                return HttpResponse("<center>Details saved successfully</center>")
            else:
                return HttpResponse("<center>Save failed!!</center>")

        returnUrl = "http://www.google.com/"
        negativeResponse = "<center><h3>This user doesn't exist. Please consider signing up or try again.</h3><a href="">Try again</a></center>"
        wrongPassResponse = "<center><h3>Wrong password.</h3><a href="">Try again</a></center>"
        if loginType == "userlogin":
            try:
                userdetails = UserDetails.objects.get(username=username)
            except:
                return HttpResponse(negativeResponse)
            saved_password = userdetails.password
            response = HttpResponseRedirect(returnUrl)
            response.set_cookie('last_connection', datetime.datetime.now())
            response.set_cookie('username', username)
            if saved_password == request.POST['password']:
                return response
            else:
                return HttpResponse(wrongPassResponse)
        else:
            try:
                admindetails = AdminDetails.objects.get(username=username)
            except:
                return HttpResponse(negativeResponse)
            saved_password = admindetails.password
            modelsActiveStatus_all = ModelsActiveStatus.objects.all()
            template = loader.get_template("Login/AdminPanel.html")
            context = {
                'modelsActiveStatus_all': modelsActiveStatus_all,
            }
            response = HttpResponse(template.render(context,request))
            if saved_password == request.POST['password']:
                return response
            else:
                return HttpResponse(wrongPassResponse)
    else:
        return render(request, 'Login/updatedloginform.html')

#******************************************************************************

@csrf_exempt 
@api_view(['GET', 'POST', ])
def SmartphoneLogin(request):
    if request.POST:
        print(request.POST)
        negativeResponse = "failed"
        wrongPassResponse = "failed"
        username=""
        if 'username' in request.POST and 'loginType' in request.POST and 'password' in request.POST:
            try:
                username = request.POST['username']
                print("Username: "+username)
                admindetails = AdminDetails.objects.get(username=username)
            except:
                print("No such admin exists")
                return HttpResponse(negativeResponse)
            if "device" in request.POST and "statusString" in request.POST:
                if request.POST['device'] == "phone":
                    try:
                        user = ModelsActiveStatus.objects.get(username=request.POST['user'])
                        user.statusString = request.POST["statusString"]
                        print(user)
                        if admindetails.password == request.POST['password']:
                            print("Saved")
                            user.save()
                            return HttpResponse("saved")
                        else:
                            print("Incorrect password")
                            return HttpResponse("Incorrect admin details")
                    except:
                        print("Setting for this user don't exist")
                        return HttpResponse("Setting for this user don't exist")
                else:
                    print("Failed")
                    return HttpResponse(negativeResponse)
            else:
                saved_password = admindetails.password
                modelsActiveStatus_all = ModelsActiveStatus.objects.all()
                serializer = StatusSerializer(modelsActiveStatus_all, many=True)
                print(serializer.data)
                response = Response(serializer.data)
                if saved_password == request.POST['password']:
                    return response
                else:
                    print("Failed")
                    return HttpResponse(wrongPassResponse)
        else:
            print("username, loginType or password missing")
            return HttpResponse(negativeResponse)
    else:
        print("Failed")
        return HttpResponse("<center>Invalid request</center>")

#***************************************************************************************

@csrf_exempt
@api_view(['GET', 'POST', ])
def FetchLogs(request):
    print("Log fetch request")
    logs = Logs.objects.all()
    serializer = LogSerializer(logs, many=True)
    return Response(serializer.data)


