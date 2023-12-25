# cvapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import CV

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'education', 'experience', 'skills']

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')