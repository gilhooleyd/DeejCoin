from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime
from userbase.forms import UserForm, TransactionForm
from userbase.models import Transaction, Person

def index(request):
    return HttpResponse("Yo, its the homepage")

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'userbase/register.html',
            {'user_form': user_form, 'registered': registered},
            context)
    
def user(request, name):
    user  = User.objects.filter(username=name)[0]
    person = user.person
    latest_transaction_list = person.transactions.order_by('-date')[:5]
    context =  {
        'latest_transaction_list': latest_transaction_list,
        'user': user,
        }
    return render(request, 'userbase/userpage.html', context)

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
		else:
			print form.errors
	
	# HTTP GET: Just get the form data
	else:
		form = TransactionForm()
	
	# Render the page
	return render(request, 'userbase/create_transaction.html',
			{'transaction_form': form})

