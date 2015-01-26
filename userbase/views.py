from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from userbase.models import Transaction, Person
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse

from userbase.forms import UserForm, LoginForm

def index(request):
    if request.user.is_authenticated():
        return HttpResponse("YAY LOGGED IN " + request.user.username)
    return HttpResponse("Yo, its the homepage")

def register(request):
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            person = Person(user=user)
            person.save()
            user.save()
            registered = True

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
    
    return render(request,
            'userbase/register.html',
            {'user_form': user_form, 'registered': registered})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_form = LoginForm(data=request.POST)
        user = authenticate(username=username, password=password)
        if login_form.is_valid():
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
    else:
        login_form = LoginForm()
        
    return render(request, 'userbase/login.html',
                      {'login_form': login_form})
        
def user(request, name):
    user  = User.objects.filter(username=name)[0]
    person = user.person
    latest_transaction_list = person.transactions.order_by('-date')[:5]
    context =  {
        'latest_transaction_list': latest_transaction_list,
        'user': user,
        }
    return render(request, 'userbase/userpage.html', context)
