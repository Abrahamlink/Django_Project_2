from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Member


class LoginForm(AuthenticationForm):
    # class Meta:
    #     model = Member
    #     fields = ('username', 'password')

    def login(self):
        print(self.cleaned_data)
