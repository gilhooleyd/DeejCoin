from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from userbase.models import Transaction, Person
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Yo, its the homepage")

def user(request, name):
    print(name)
    user  = User.objects.filter(username=name)[0]
    person = user.person
    print(user.username)
    print(person.coins)
    latest_transaction_list = person.transactions.order_by('-date')[:5]
    actual_list = []
    for transaction in latest_transaction_list:
        people = transaction.person_set.all()
        actual_list.append([people[0].user.username, people[1].user.username, transaction.amount, transaction.date])
    if (actual_list):
        print (actual_list)
    context =  {
        'latest_transaction_list': actual_list,
        'user': user,
        }
    return render(request, 'userbase/userpage.html', context)
