from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms


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
        cleaned_data = super(LoginForm, self).clean()
        u = self.cleaned_data.get('username')
        p = self.cleaned_data.get('password')
        #print (u + "  " + p)
        if authenticate(username=u, password=p):
            return u
        else:
            raise forms.ValidationError("Incorrect username or password")
