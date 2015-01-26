from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.urlresolvers import reverse
from userbase.models import Person
from userbase.forms import UserForm, LoginForm, TransactionForm
from datetime import datetime

def redirect_if_logged_in(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('user', args=(request.user.username,)))

def index(request):
    if request.user.is_authenticated():
        print(request.user.username)
        return HttpResponseRedirect(reverse('user', args=(request.user.username,)))
    return HttpResponseRedirect(reverse('homepage'))


def register(request):
    redirect_if_logged_in(request)
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
            login(request, user)
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
    
    return render(request,
            'userbase/register.html',
            {'user_form': user_form, 'registered': registered})

def user(request, name):
    userlist = User.objects.filter(username=name)
    if (len(userlist) < 1): 
        return HttpResponse("There's nobody with that username!")
    user = userlist[0]
    person = user.person
    is_homepage = request.user.username == name
    latest_transaction_list = person.transactions.order_by('-date')[:5]
    context =  {
        'latest_transaction_list': latest_transaction_list,
        'user': user,
        'active_user': request.user,
        'is_homepage': is_homepage,
        }
    return render(request, 'userbase/userpage.html', context)

def user_login(request):
    redirect_if_logged_in(request)
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
        
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

def create_transaction(request, name):
	# HTTP POST: Submit data
	if request.method == 'POST':
		form = TransactionForm(request.POST)
		if form.is_valid():
			transaction = form.save()
			transaction.amount = request.POST['amount']
			transaction.date = datetime.now()
			transaction.save()
			giver = User.objects.filter(username=name)[0]
			giver = Person.objects.filter(user=giver)[0]
			recipient = User.objects.filter(username=request.POST['recipient'])[0]
			recipient = Person.objects.filter(user=recipient)[0]
			giver.transactions.add(transaction)
			recipient.transactions.add(transaction)
                        redirect_if_logged_in(request)
		else:
			print form.errors
	
	# HTTP GET: Just get the form data
	else:
		form = TransactionForm()
	
	# Render the page
	return render(request, 'userbase/create_transaction.html',
			{'transaction_form': form})

def leaderboard(request):
    people = Person.objects.all().order_by('-coins')
    return render(request, 'userbase/leaderboard.html', {'people': people,
                                                         'active_user': request.user})
