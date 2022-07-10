from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Shorter_history

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )

class ShorterHistoryForm(forms.ModelForm):
    class Meta:
        model = Shorter_history
        fields = ['user_id', 'user_url', 'short_url']