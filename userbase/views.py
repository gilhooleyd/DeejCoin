from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from userbase.models import Transaction, Person
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Yo, its the homepage")

def user(request, name):
    user  = User.objects.filter(username=name)[0]
    person = user.person
    latest_transaction_list = person.transactions.order_by('-date')[:5]
    context =  {
        'latest_transaction_list': latest_transaction_list,
        'user': user,
        }
    return render(request, 'userbase/userpage.html', context)
