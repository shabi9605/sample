from os import name
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.cache import cache 
import datetime
from shabi import settings


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return str(self.name)


class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    phone=PhoneNumberField()
    status=models.BooleanField(default=False)
    programmer='programmer'  #in quotes , that is used to represent the type or name
    project_manager='project_manager'

    user_types=[
        (programmer,'programmer'),
        (project_manager,'project_manager')
    ]

    user_type=models.CharField(max_length=30,choices=user_types,default=programmer)

    def __str__(self):
        return str(self.user.username)

    

    
class Image(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    

class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now,blank=True)

    def __str__(self):
        return str(self.title)





    
    