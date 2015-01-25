from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField('date published')
    def __str__(self):
        return str(self.amount)
class Person(models.Model):
    user = models.OneToOneField(User)
    coins = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    transactions = models.ManyToManyField(Transaction, blank=True)
    def __str__(self):
        return self.user.username
