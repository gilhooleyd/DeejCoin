from django.db import models
from django.contrib.auth.models import User

class Bounty(models.Model):
    posted = models.DateTimeField('date posted', default=datetime.now)
    amount = models.IntegerField(default=0)
    message = models.CharField(max_length=500)        
    user = models.ManyToManyField(User)

