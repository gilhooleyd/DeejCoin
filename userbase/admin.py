from django.contrib import admin
from userbase.models import Transaction, Person, LevelUp
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
admin.site.register(LevelUp)
