from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field-input'}),label='Create Username')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'field-input'}),label='Create Email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Create password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Repeat password')


    class Meta:
        model = User
        fields = ['username','email','password1']



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'field-input'}),label='Enter your username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'field-input'}),label='Enter Password')


    class Meta:
        model = User
        fields = ['username','password']