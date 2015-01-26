from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField('date published', default=datetime.now)
    def __str__(self):
		if (len(self.person_set.all()) != 2):
			return str(self.amount)
		trans_str =  self.person_set.all()[0].user.username + " => "
		trans_str += self.person_set.all()[1].user.username + ": " 
		trans_str += str(self.amount)
		return trans_str

class Person(models.Model):
    user = models.OneToOneField(User)
    coins = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    transactions = models.ManyToManyField(Transaction, blank=True)
    def __str__(self):
        return self.user.username

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
