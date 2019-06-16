from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
# Create your views here.


def logout_request(request):
    logout(request)
    return redirect('users:signin')


def signup(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get('username')
        messages.success(
            request, f'Account has been created successfully for {user}')
        return redirect('users:signin')
    return render(request, 'users/signup.html', context={
        'form': form
    })


def signin_request(request):
    if request.method == 'POST':
        forms = AuthenticationForm(request, request.POST)
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(
                    request, f'You have been successfully logged in as {username}')
                return redirect('tutorial:home')
            else:
                messages.error(
                    request, 'There was an error in your password and email!')
    else:
        forms = AuthenticationForm()
    return render(request, 'users/signin.html', context={
        'form': forms
    })
