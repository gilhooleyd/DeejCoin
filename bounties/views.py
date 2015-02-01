from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from bounties.models import Bounty
from bounties.forms import CreateBounty


def createBountyPage(request):
    error_msg = []
    if request.method == 'POST':
        form = CreateBounty(request.POST)
        if form.is_valid():
            bounty = form.save()
            bounty.user.add(request.user)
