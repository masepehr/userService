from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.views.generic import UpdateView

from UserService.models import Profile, Adress


class signUpForm(UserCreationForm):

    username=forms.CharField(max_length=255, help_text='ضروری .حداکثر 150 کاراکتر')
    first_name = forms.CharField(max_length=255, required=False, help_text='اختیاری')
    last_name = forms.CharField(max_length=255, required=False, help_text='اختیاری')
    email = forms.EmailField(max_length=255, help_text='لطفا ایمیل به فرمت مناسب استفاده شود')
    birthdate = forms.DateField(help_text='(ex: 1988-02-02)')

    class Meta:

        model=User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','birthdate', )


# class profileForm(forms.ModelForm):
#     username=forms.CharField(disabled=True)
#     last_name = forms.CharField(max_length=255, required=False, help_text='اختیاری')
#     first_name = forms.CharField(max_length=255, required=False, help_text='اختیاری')
#     email = forms.EmailField(max_length=255)
#
#     class Meta:
#         model=User
#         fields = ['username', 'first_name', 'last_name', 'email']

class loginForm(AuthenticationForm):
    username = forms.CharField

