from django.contrib.auth.models import User
from django import forms
from models import Transaction

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class TransactionForm(forms.ModelForm):
	user_choices = []
	for user in User.objects.all():
		new_choice = (user.username, user.username)
		user_choices.append(new_choice)
	recipient = forms.ChoiceField(choices=user_choices)
	class Meta:
		model = Transaction
		fields = ('amount',)
