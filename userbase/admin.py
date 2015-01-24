from django.contrib import admin
from userbase.models import Transaction, User
# Register your models here.
#class TransactionInLine(admin.StackedInLine):
#    model = Transaction
#    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('NAME:',    {'fields' : ['name']}),
        ('ITEMS:',   {'fields' : ['coins', 'level']}),
        ]
#    inlines = [TransactionInLine]

admin.site.register(User, UserAdmin)
admin.site.register(Transaction)
