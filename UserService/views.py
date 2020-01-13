from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .forms import *
from django.shortcuts import render, redirect


# Create your views here.

def signup(request):
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=signUpForm(request.POST)

        if form.is_valid() :
            user=form.save()
            user.refresh_from_db()
            user.profile.birthdate=form.cleaned_data['birthdate']
            user.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')


    else:
        form=signUpForm()
    return render(request,'signup.html',{'form':form})






def home(request):
    return render(request,'index.html')