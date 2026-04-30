from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from .forms import UserRegisterForm, UserUpdateForm

def register_user(request):
    form = UserRegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account has been created for {username}')
        return redirect('login')

    return render(request, 'user-temp/register.html', {'form': form})


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        return redirect('home')

    return render(request, 'user-temp/login.html', {'form': form})

def logout_user(request):
    auth.logout(request)
    return render(request, 'user-temp/logout.html')

@login_required(login_url='login')
def profile(request):
    up_form = UserUpdateForm(request.POST or None, instance=request.user)

    if request.method == 'POST' and up_form.is_valid():
        up_form.save()
        messages.success(request, 'Your account has been updated!')
        return redirect('profile')

    return render(request, 'user-temp/profile.html', {'up_form': up_form})
