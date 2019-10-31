from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserDetails, AdminDetails
import datetime
from django.template import loader

def ShowLoginPage(request):
    if request.POST:
        username = request.POST['username']
        loginType = request.POST['loginType']

        returnUrl = ""
        if loginType == "userlogin":
            try:
                userdetails = UserDetails.objects.get(username=username)
                returnUrl = "http://www.google.com/"
            except:
                return HttpResponse("<center><h3>This user doesn't exist. Please consider signing up or try again.</h3><a href="">Try again</a></center>")
            saved_password = userdetails.password
        else:
            try:
                admindetails = AdminDetails.objects.get(username=username)
                returnUrl = "http://duckduckgo.com/"
            except:
                return HttpResponse("<center><h3>This user doesn't exist. Please consider signing up or try again.</h3><a href="">Try again</a></center>")
            saved_password = admindetails.password
        
        if saved_password == request.POST['password']:
            response = HttpResponseRedirect(returnUrl)
            response.set_cookie('last_connection', datetime.datetime.now())
            response.set_cookie('username', username)
            return response
        else:
            return HttpResponse("<center><h3>Wrong password.</h3><a href="">Try again</a></center>")         
    return render(request, 'Login/updatedloginform.html')


