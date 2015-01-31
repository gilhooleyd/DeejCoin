from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from models import Transaction, Person


class UserForm(forms.ModelForm):
    min_username_length = 5
    min_password_length = 5
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if len(username) < self.min_username_length:
            raise forms.ValidationError("Username must have at least %i characters" % self.min_username_length)
        else:
            return username

    def clean_password(self):
        p = self.cleaned_data.get('password', '')
        if len(p) < self.min_password_length:
            raise forms.ValidationError("Password must have at least %i characters" % self.min_username_length)
        else:
            return p

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        super(LoginForm, self).clean()
        u = self.cleaned_data.get('username')
        p = self.cleaned_data.get('password')
        if authenticate(username=u, password=p):
            return u
        else:
            raise forms.ValidationError("Incorrect username or password")

class TransactionForm(forms.ModelForm):
    # this method is needed to run EVERY form, otherwise choices are cached
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TransactionForm, self).__init__(*args, **kwargs)
        person_choices = []
        for person in sorted(Person.objects.all()):
            if user and user.username == person.user.username:
                continue
            new_choice = (person.user.username, person.user.username)
            person_choices.append(new_choice)
        # Sort choices by username
        self.fields['recipient'].choices = \
                sorted(person_choices, key=lambda x: x[1])
    recipient = forms.ChoiceField()
    amount = forms.IntegerField(min_value=1)
    message = forms.CharField(required=False, max_length=100,
           widget=forms.TextInput(attrs={'size': '60'}))
    class Meta:
        model = Transaction
        fields = ('amount', )            
