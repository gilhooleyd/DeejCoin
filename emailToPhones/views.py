from django.shortcuts import render
from emailsToPhones.models import Number
from django.core.mail import send_mail

def sendMessage(request, name):
    user = User.objects.filter(username=name)
    if (len(userlist) < 1):
        return HttpResponse("There's nobody with that username!")
    user = user[0]

    address = str(user.number)

    
    
