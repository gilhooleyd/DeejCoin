from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Transaction(models.Model):
    amount = models.IntegerField(default=1)
    date = models.DateTimeField('date published', default=datetime.now)
    message = models.CharField(default='', max_length=100)
    def __str__(self):
		if (len(self.person_set.all()) != 2):
			return str(self.amount)
		trans_str =  self.person_set.all()[0].user.username + " => "
		trans_str += self.person_set.all()[1].user.username + ": " 
		trans_str += str(self.amount)
		if (self.message):
			trans_str += " | \"" + self.message + "\""
		return trans_str

class Person(models.Model):
    user = models.OneToOneField(User)
    coins = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    transactions = models.ManyToManyField(Transaction, blank=True)
    def __str__(self):
        return self.user.username
