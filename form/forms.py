from django import forms
from django.forms import fields
from . models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    username=forms.CharField(help_text=None,label='Username')
    password1=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Password')
    password2=forms.CharField(help_text=None,widget=forms.PasswordInput,label='Confirm Password')
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')
        labels=('password1','Password','password2','Confirm_Password')



class ProfileForm(forms.ModelForm):
    address=forms.Textarea()
    programmer='programmer'
    user_types=[
        (programmer,'programmer') 
    ]
    user_type=forms.ChoiceField(required=True,choices=user_types)
    class Meta:
        model=Register
        fields=('address','phone','user_type')


class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('name','image')


class TodoUpdateForm(forms.ModelForm):
    title=forms.CharField(max_length=50)
    content=forms.Textarea()
    date=forms.DateTimeField(required=False)
    class Meta:
        model=Todo
        fields=('title','content','date')