from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_layout(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'No te has identificado correctamente')



    return render(request, 'login_layout.html', {
        'title' : "Login"
    })

def logout_user(request):
    logout(request)
    return redirect('login')

def loged(request):
    usuario = request.user
    return render(request, 'loged.html', {
        'usuario' : usuario,
        'title' : 'Loged'
    })