from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def index(request):
    return render(request, 'deejCoin/index.html')
    
