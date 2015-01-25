from django.contrib import admin
from django.contrib.auth.models import User
from userbase.models import Transaction, Person
# Register your models here.
#class TransactionInLine(admin.StackedInLine):
#    model = Transaction
#    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User:',    {'fields' : ['user']}),
        ('ITEMS:',   {'fields' : ['coins', 'level']}),
        ('TRANSACTIONS:', {'fields' : ['transactions']}),
        ]
#    inlines = [TransactionInLine]

admin.site.register(Person, UserAdmin)
admin.site.register(Transaction)
