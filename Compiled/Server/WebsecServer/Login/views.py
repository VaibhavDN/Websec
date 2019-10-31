from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import UserDetails
import datetime

def ShowLoginPageUser(request):
    if request.POST:
        username = request.POST['username']
        try:
            userdetails = UserDetails.objects.get(username=username)
        except:
            return HttpResponse("<center><h3>This user doesn't exist. Please consider signing up or try again.</h3><a href="">Try again</a></center>")
        saved_password = userdetails.password
        if saved_password == request.POST['password']:
            response = HttpResponseRedirect("http://www.google.com/")
            response.set_cookie('last_connection', datetime.datetime.now())
            response.set_cookie('username', username)
            return response
        else:
            return HttpResponse("<center><h3>Wrong password.</h3><a href="">Try again</a></center>")         
    return render(request, 'Login/updatedloginform.html')

def ShowLoginPageAdmin(request):
    return HttpResponse("Admin Page")

