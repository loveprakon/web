from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def hello(request):
    # Query from model
    data = Post.objects.all()
    return render(request, 'index.html', {'posts':data})

# Create your views here.
def page1(request):
    return render(request, 'page1.html')

def createForm(request):
    return render(request, 'form.html')

def adduser(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password = request.POST['password']
    repassword = request.POST['repassword']
    if (password == repassword):
        if User.objects.filter(username=username).exists():
            print('user มีคนใช้แล้ว')
            messages.info(request, 'user มีคนใช้แล้ว')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            print('Email มีคนใช้แล้ว')
            messages.info(request, 'Email มีคนใช้แล้ว')
            return redirect('/createForm')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
                )
            user.save()
            return redirect('/')

    else:
        messages.info(request, 'รหัสผ่านไม่ตรงกัน')
        return redirect('/createForm')

def loginform(request):
    return render(request, 'login.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)
    "user has in system"
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'รหัสผ่านผิด')
        return redirect('/loginForm')

def logout(request):
    auth.logout(request)
    return redirect('/')