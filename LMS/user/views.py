from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import authenticate , login,logout
from .forms import newuserform
from django.contrib.auth.models import User

def hello(request):
    return render (request,'user/home-v7.html')

# Create your views here.
def login(request):
    '''
    if request.method =="POST":
        username = request.POST.get('username') 
        password= request.POST.get('password')
        user12 = authenticate(request,name=username, password=password)
        print(username,password)
        if user12 is not None:
            login(request,user12)
            return redirect ('/login')
        else:
            #messages.success(request, 'there is trouble logging in....')
            return redirect('/profile')

    else:'''
    return render(request,'user/login.html')
    

def logout_user(request):
        logout(request)
        #messages.success(request, 'You Logged out')
        return redirect('/')      
    
def profile(request):
        return render(request,'user/profile.html')

def courselist(request):
        return render(request,'user/course-list-v3.html')

def register(request):
    if request.method =="POST":
        form = newuserform(request.POST)
        if form.is_valid():
            user=form.save()
            
            username = form.cleaned_data['userSname']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            #messages.success(request, 'Registration Successful..')
            return redirect('/')
        else:
            form = newuserform() 

    return render(request,'user/register.html',locals())

