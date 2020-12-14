from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'myblog/index.html')

@login_required(login_url = 'signin')
def dashboard(request):
    return render(request, 'myblog/dashboard.html')

@login_required(login_url = 'signin')
def profile(request):
    return render(request, 'myblog/profile.html')

def signup(request):
    if request.method == 'POST':        
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, 'Account created for' + username)
            return redirect('signin')
    else:
        form = CreateUserForm()    
    return render(request, 'myblog/signup.html', {'form':form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            # form = AuthenticationForm(request.POST)
            # if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request, 'myblog/signin.html')
    
        form = AuthenticationForm()
        context = {}
        return render(request, 'myblog/signin.html', context)

@login_required(login_url = 'signin')
def logoutUser(request):
    logout(request)
    return redirect('signin')

