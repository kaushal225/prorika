from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.
def register(request):

    if request.method == "POST":
        context={'has_error':False,'data':request.POST}
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('password_confirm')
        print(password)

        if not username:
            messages.add_message(request,messages.WARNING,'please enter username')
            context['has_error']=True
        if len(password)<6:
            messages.add_message(request,messages.WARNING,'password length should be greater than 6')
            context['has_error']=True

        if password != confirm_password:
            messages.add_message(request,messages.WARNING,'password mismatch')
            context['has_error']=True
            
        if User.objects.filter(username=username).exists():
            messages.add_message(request,messages.WARNING,'username is already taken')
            context['has_error']=True

        if User.objects.filter(email=email).exists():
            messages.add_message(request,messages.WARNING,'email is already taken')
            context['has_error']=True

        if context['has_error']:
            return render(request,'authentication/registration.html',context=context)
        user=User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.save()
        return render(request,'authentication/login.html')
    return render(request,'authentication/registration.html')


def user_login(request):


    if request.method=='POST':
        
        context={'data':request.POST}

        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if not user:
            messages.add_message(request,messages.ERROR,'username or password invalid')
            return render(request,'authentication/login.html',context)
        login(request,user)
        messages.add_message(request,messages.SUCCESS,f'welcome {user.username} ')
        return redirect(reverse('home'))

    return render(request,'authentication/login.html')


def logout_user(request):
    logout(request)
    messages.add_message(request,messages.SUCCESS,'logged out successfully')
    return render(request,'authentication/login.html')