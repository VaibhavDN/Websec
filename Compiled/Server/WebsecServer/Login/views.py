from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserDetails, AdminDetails, ModelsActiveStatus
import datetime
from django.template import loader

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

def ShowLoginPage(request):
    if request.POST:
        try:
            username = request.POST['username']
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

    return render(request, 'Login/updatedloginform.html')


