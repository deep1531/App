# accounts/views.py

from django.contrib.auth import authenticate
from rest_framework import generics, status
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import NameSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from core.views import *


class Signup(generics.CreateAPIView):
    serializer_class = NameSerializer


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)  
        if user is not None:
            login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@login_required(login_url="/login_view/")
def index_view(request):
    return render(request, 'index.html')


def abc(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=Name(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Your account is successfully created!')
        return redirect('abc') 
         
        if user is None:
            messages.error(request,'Please try again.') 
            return redirect('abc') 
       
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is  None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid details. Please try again.')
    return render(request, 'login1.html')

@login_required(login_url="/login_view/")
def logout_view(request):
    logout(request)
    return redirect('login')


def update_user(request, id):   
    queryset = Name.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        queryset.username = username
        queryset.email = email

        queryset.save()
        messages.success(request, 'User updated successfully.')
        return redirect("index_two")

    context = {'Name': queryset}
    return render(request, "update_user.html", context)  


def delete_user(request, id):
    try:
        queryset = Name.objects.get(id=id)
        queryset.delete()
        messages.success(request, 'User deleted successfully.')
    except User.DoesNotExist:
        messages.error(request, 'User does not exist.')
    
    return redirect("index_two")


ADMIN_USERNAME = 'adminsingh' 
ADMIN_PASSWORD = '123@singh'
def Adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            return redirect('index_two')  
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('Adminlogin') 

    return render(request, 'login2.html')

def index_two(request):
    if request.method == "POST":
        
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')


        Name.objects.create(
            username = username,
            password = password,
            email = email,
        )
        return redirect ("index1")
    queryset = Name.objects.all()


    context = {'Names': queryset}

    return render(request, 'index1.html', context)

def logout_admin(request):
    logout(request)
    return redirect('Adminlogin')

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login_view')

