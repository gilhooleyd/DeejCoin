from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
from models import Bounty

class CreateBounty(forms.ModelForm):
    class Meta:
        model = Bounty
        fields = ('amount', 'message')

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if message < 1:
            raise forms.ValidationError("Amount must be a positive number")
        else:
            return message
