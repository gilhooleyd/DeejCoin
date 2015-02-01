from django.db import models
from django.contrib.auth.models import User

carrierToEmail = { 'AT&T': '@txt.att.net',}

class Number(models.Model):
    user = models.OneToOneField(User)
    digits = models.charField(max_length=10)
    carrier = models.charField(max_length=50)

    def __str__(self):
        return digits + "@" + carrierToEmail[carrier]
