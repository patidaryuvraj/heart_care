from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import form

def indexView(request):
    return render(request,'contact.html')



def contact(request):
    form1=form   # new change
    if request.method == 'POST':
        form1 = form(request.POST)
        if form1.is_valid():
            form1.save()
           # #return render(request,'private/addemp.html',{'empForm':EmpForm(),'msg':"Employee Added..!!"})
            return redirect('contact.html', {'msg':"Registered Successfully...!!!"}) # form is valid
        else:
            return redirect('contact.html',{'error':"Invalid User Request...!!!"}) #if form is not valid
    else:
        return redirect('contact.html' ,{'error':"Invalid User Request...!!!"})# all condition false
