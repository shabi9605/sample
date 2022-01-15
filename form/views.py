from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . models import *
from . forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get("email")
        mesg=request.POST.get("msg")

        Contact.objects.create(
            name=name, #first is database field name and second is get cheytha field name
            email=email,
            message=mesg
        )
        return render(request,'contact.html',{'msg':'successfully added'})
    return render(request,'contact.html')


def register(request):
    reg=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            reg=True
        else:
            return HttpResponse("Invalid Form")
    else:
        user_form=UserForm()
        profile_form=ProfileForm()

    return render(request,'register.html',{'register':reg,'user_form':user_form,'profile_form':profile_form})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        active=Register.objects.all().filter(user_id=user.id,status=True)
        if user:
            if user.is_active and active and not user.is_superuser:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))
            elif user.is_active and user.is_superuser:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))       
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request,'login.html')


def dashboard(request):
    list=Todo.objects.all()
    return render(request,'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')



def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCESSFULLY UPDATED")
            return render(request,'change_password.html')
        else:
            messages.error(request,"PLEASE CORRECT ERROR")
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{"form":form})

def image_upload(request):
    if request.method=="POST":
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            imgage_obj=form.instance
            return render(request,'image_upload.html',{'form':form,'image_obj':imgage_obj})

        else:
            return HttpResponse('invalid form')

    else:
        form=ImageForm()
    return render(request,'image_upload.html',{'form':form})


def myblog(request):
    myblogs=Todo.objects.filter(user=request.user).order_by('date')
    print(request.user)
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        date=request.POST.get('date')

        Todo.objects.create(
            title=title,
            content=content,
            date=date,
            user=request.user
        )
        return redirect('myblog')

    else:
        return render(request,'todo_list.html',{'todolist':myblogs})



def myblogupdate(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    form=TodoUpdateForm(instance=todo)
    if request.method=="POST":
        form=TodoUpdateForm(request.POST,instance=todo)
        form.save()
        return redirect('myblog')
    
    return render(request,'update.html',{'form':form})


def myblogdelete(request,todo_id):
    deleteitem=Todo.objects.get(id=todo_id)
    deleteitem.delete()
    return redirect('myblog')

def image_download(request):
    img_download=Image.objects.all()
    return render(request,'image_download.html',{'img_down':img_download})

def profile(request):
    users=Register.objects.all()
    return render(request,'profile.html',{'users':users})









