from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)

    return redirect('/')

def log_out(request):
    logout(request)
    return redirect('/')
