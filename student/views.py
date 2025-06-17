from django.shortcuts import render
from .form import Show_detelis
from django.http import HttpResponseRedirect
# Create your views here.
def data(req):
    if req.method =='POST':
        form=Show_detelis(req.POST)
        if form.is_valid():
            NAME=form.cleaned_data['NAME']
            ROLL_number=form.cleaned_data['ROLL_number']
            password=form.cleaned_data['password']
            print('Name',NAME)
            print('Email',ROLL_number)
            print('Password',password)
            form=Show_detelis()
            return HttpResponseRedirect('/student/success/')
    else:
        form=Show_detelis()
    return render(req,'student/index.html',
                  
    {'form':form})

def req_sucess(req):
    return render(req,('student/sucess.html'))