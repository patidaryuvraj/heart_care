from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
     return render(request,'index.html')
def home(request):
     return render(request,'index.html')
def doctor(request):
     return render(request,'doctors.html')
def services(request):
     return render(request,'services.html')
def contact(request):
     return render(request,'contact.html')
def appointment(request):
     return render(request,'appointment.html')
def signupPage(request):
     return render(request,'signup.html')
def signinPage(request):
    return render(request,'signin.html')


def signUp(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        unm = request.POST['username'] #ABC123
        pwd = request.POST['password']
        try :
                user = User.objects.get(email=email)
                return render(request,'signup.html',{'error':"Email Already Exists...!!!"})
        except :
            user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=unm,password=pwd)   
            user.save()
            return render(request,'signin.html',{'msg':"Registered Successfully...!!!"})
    else:
        return render(request,'signup.html',{'error':"Invalid User Request...!!!"})

def signin(request):
    if request.method =="POST":
        unm=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=unm,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'appointment.html',{'msg': "Logedin successfully.."})  #if login details correct redirect to appointment page
        else:
            return render(request,'signin.html' ,{'error':"Invalid User Request...!!!"})  #else relod the page
    else:
        return render(request,'signin.html' ,{'error':"Invalid User Request...!!! "})  #else relod the page
    
def userhome(request):
    return render(request,'userhome.html')
