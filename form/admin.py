from django.contrib.admin.decorators import register
from form.views import contact
from django.contrib import admin
from . models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(Contact,ContactAdmin)
admin.site.register(Register)
admin.site.register(Image)

class TodoAdmin(admin.ModelAdmin):
    list_display=('user','title','content','date')

admin.site.register(Todo,TodoAdmin)
