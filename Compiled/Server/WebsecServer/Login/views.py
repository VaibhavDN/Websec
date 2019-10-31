from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserDetails, AdminDetails
import datetime
from django.template import loader

def ShowLoginPage(request):
    if request.POST:
        username = request.POST['username']
        loginType = request.POST['loginType']

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
            response = render(request, "Login/AdminPanel.html")
            if saved_password == request.POST['password']:
                return response
            else:
                return HttpResponse(wrongPassResponse)

    return render(request, 'Login/updatedloginform.html')


