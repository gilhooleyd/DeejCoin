from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    coins = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Transaction(models.Model):
    userThis = models.ForeignKey(User)
    userOther = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    withdraw = models.BooleanField()
    date = models.DateTimeField('date published')
    def __str__(self):
        return self.userThis.name
