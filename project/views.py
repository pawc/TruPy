from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)

    return redirect('/trupy')

@csrf_exempt
def log_out(request):
    logout(request)
    return redirect('/trupy')
