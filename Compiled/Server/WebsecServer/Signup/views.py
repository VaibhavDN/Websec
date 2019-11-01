from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from Login.models import UserDetails, ModelsActiveStatus

def ShowSignupPage(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            userdetails = UserDetails.objects.get(username=username)
            return HttpResponse("<center><h3>This user already exists. Try again with different username.</h3><a href="">Try again</a></center>")
        except:
            if request.POST['password'] == request.POST['repassword']:
                userdetails = UserDetails()
                userdetails.username = username
                userdetails.password = password
                userdetails.save()
                modelsActiveStatus = ModelsActiveStatus()
                modelsActiveStatus.username = username
                modelsActiveStatus.statusString = "1111111111"
                modelsActiveStatus.save()
                return HttpResponseRedirect("http://127.0.0.1:8000/login/")
            else:
                return HttpResponse("<center><h3>Password mismatch!.</h3><a href="">Try again</a></center>")            
    return render(request, 'Signup/updatedsignupform.html')

