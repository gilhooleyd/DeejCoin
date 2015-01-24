from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from userbase.models import Transaction, User

def index(request):
    return HttpResponse("Yo, its the homepage")

def user(request, name):
    print(name)
    user = User.objects.filter(name=name)[0]
    print(user.name)
    print(user.coins)
    latest_transaction_list = Transaction.objects.filter(userThis=user).order_by('-date')[:5]
    
    context =  {
        'latest_transaction_list': latest_transaction_list,
        'user': user,
        }
    return render(request, 'userbase/userpage.html', context)
