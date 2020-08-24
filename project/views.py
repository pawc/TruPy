from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect

def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        return redirect('/trupy')
    else:
        response = HttpResponse()
        response.status_code = 401
        return response
