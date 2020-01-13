from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class signUpForm(UserCreationForm):

    username=forms.CharField(max_length=255, help_text='ضروری .حداکثر 150 کاراکتر')
    first_name = forms.CharField(max_length=255, required=False, help_text='اختیاری')
    last_name = forms.CharField(max_length=255, required=False, help_text='اختیاری')
    email = forms.CharField(max_length=255, help_text='لطفا ایمیل به فرمت مناسب استفاده شود')
    class Meta:

        model=User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )