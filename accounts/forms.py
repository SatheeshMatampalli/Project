from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import *
from django.forms import ModelForm
from django import forms

class UserForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"placeholder":"enter passord1"
		})
		)
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']
		widgets={
		"username":forms.TextInput(attrs={
			"placeholder":"enter first_name",
			"required":True,
			"class":"form-control"
			}),
		"first_name":forms.TextInput(attrs={
			"placeholder":"enter firstname",
			"class":"form-control"
			})
		
		}

class ContactForm(ModelForm):
	class Meta:
		model=Contact
		fields='__all__'
