from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, models
from django.contrib.auth.models import User
from django.db import models


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username =  request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect('blog-home')
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

def profile(request):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    return render(request, 'users/profile.html')