from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
        else:
            messages.warning(request, "Error!")
        return redirect('home')

    context = {}
    return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You've registered successfully!")
            return redirect('home')

    form = SignupForm()
    context = {'form': form}
    return render(request, 'register.html', context)
