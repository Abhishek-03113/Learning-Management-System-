from django.shortcuts import render ,HttpResponse,redirect
from django.contrib.auth import authenticate , login,logout

def hello(request):
    return render (request,'user/home.html')

# Create your views here.
def login(request):
    
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

    else:
        return render(request,'user/login.html')
    

def logout_user(request):
        logout(request)
        #messages.success(request, 'You Logged out')
        return redirect('/')      
    
def profile(request):
        return render(request,'user/profile.html')