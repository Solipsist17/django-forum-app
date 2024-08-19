from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Category
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def feed(request):
    return render(request, 'feed.html')

# registrarse
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # register user
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)    # guardamos la cookie de inicio de sesión
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'Username already exists'
                })
        
        return  render(request, 'signup.html', {
                        'form': UserCreationForm,
                        'error': 'Password do not match'
                })

# cerrar sesión    
def signout(request):
    logout(request)
    return redirect('home')

# iniciar sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], 
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or Password is incorrect'
            }) 
        else:
            login(request, user)
            return redirect('feed')
    
def create_category(request):
    Category.objects.create(name='category1', description='description_category1')
    return HttpResponse('category created!')

def categories(request):
    categories = Category.objects.all()
    return HttpResponse(categories)