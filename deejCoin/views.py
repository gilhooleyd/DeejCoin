from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
