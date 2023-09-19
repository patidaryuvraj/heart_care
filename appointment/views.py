
# Create your views here.
from django.shortcuts import render,redirect

# Create your views here..
from .forms import form
from .models import appoint

# def add(request):
#     form1 = form()
#     return render(request,'userhome.html',{'form1':form1})
def insert(request):
    form1=form   # new change
    if request.method == 'POST':
        form1 = form(request.POST)
        if form1.is_valid():
            form1.save()
           # #return render(request,'private/addemp.html',{'empForm':EmpForm(),'msg':"Employee Added..!!"})
            return redirect('appointment.html', {'msg':"Registered Successfully...!!!"}) # form is valid
        else:
            return redirect('appointment.html',{'error':"Invalid User Request...!!!"}) #if form is not valid
    else:
        return redirect('appointment.html' ,{'error':"Invalid User Request...!!!"})# all condition false
