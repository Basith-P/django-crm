from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import *
from .models import Record


def home(request):
    records = Record.objects.all()

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

    context = {'records': records}
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


def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record of {record} deleted")
    else:
        messages.warning(request, "You don't have access to do that")
    return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.warning(request, "You Must Be Logged In...")
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Has Been Updated!")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.warning(request, "You Must Be Logged In...")
        return redirect('home')
