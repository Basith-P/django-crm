from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
        else:
            messages.success(request, "Error!")
        return redirect('home')

    context = {}
    return render(request, 'home.html', context)


def login_view(request):
    pass


def logout_view(request):
    pass
