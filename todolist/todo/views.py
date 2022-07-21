from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import List_model
from django.contrib.auth.decorators import login_required,user_passes_test



@login_required(login_url='login_view')
def base(request):
    return render(request,"base.html")

@login_required(login_url='login_view')
def index(request):
    user_work=List_model.objects.filter(username=request.user).values()
    context = {
    'user_work': user_work,
  }
    return render(request,"index.html",context)




def login_view(request):
    return render(request,"login.html")

def signup_view(request):
    return render(request,"signup.html")

def register_user(request):

    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        if not(User.objects.filter(username=username).exists()):
            user = User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname)
            user.save()
            login(request,user)
            # return render(request,"base")
            return HttpResponseRedirect(reverse("index"))
        else:
            print("Already exists!!!!!!")
            return HttpResponseRedirect(reverse("signup_view"))
    return HttpResponseRedirect(reverse("signup_view"))
        
def login_user(request):
    if request.method=="POST":
        
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse("login_view"))
    else:
        print("Can't Login")
        return HttpResponseRedirect(reverse("signup_view"))
    return HttpResponseRedirect(reverse("signup_view"))



def logout_view(request):
    logout(request)
    return  HttpResponseRedirect(reverse("login_view"))


def add_work(request):
    if request.method=="POST":
        username=request.POST['username']
        work=request.POST['subject']
        date=request.POST['date']
        time=request.POST['time']
        member=List_model(username=username,work=work,setting_date=date,setting_time=time)
        member.save()
        return  HttpResponseRedirect(reverse("index"))
    return  HttpResponseRedirect(reverse("index"))

def delete(request, id):
  member = List_model.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))