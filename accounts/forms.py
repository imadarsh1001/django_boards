from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # CHOICES=[('s','select 1'),('m','selct 2')]
    # like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(),required=True)
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    phone= forms.RegexField(regex='^[789]\d{9}$')
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = User
        fields = ('phone','date','username', 'email', 'password1', 'password2')