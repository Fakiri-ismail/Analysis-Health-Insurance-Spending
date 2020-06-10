from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username=forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={"class":"from-control"}))
    password=forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"class":"from-control"}))

class SingUpForm(UserCreationForm):
    username=forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={"class":"from-control"}))
    email=forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"from-control"}))
    password1=forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={"class":"from-control"}))
    password2=forms.CharField(label="Confirmer le Mot de passe", widget=forms.PasswordInput(attrs={"class":"from-control"}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')