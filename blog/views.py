from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib import auth
from collections import OrderedDict
from blog.fusioncharts import FusionCharts
from django.views import generic
from service.models import Bureau, Intervenant
from intervention.models import Intervention, Panne
from .models import Email
from .forms import EmailForm, ChatForm, SignUpForm, forms
from blog.forms import UserForm,UserProfileInfoForm



from .models import Article

def index (request):
    
   
    return render(request, 'blog/Index.html')

def accueill (request):
    
   
    return render(request, 'blog/Accueil1.html')


def accueil (request):
    return render(request, 'blog/Accueil.html')

def contact (request):
    return render(request, 'blog/Contact.html')


def contactview (request):
    return render(request, 'blog/ContactView.html')

def email_detail (request):
    email= Email.objects.all()
    return render(request, 'blog/Inbox.html',{'email':email})


def lock (request):
    return render(request, 'blog/Lock.html')

def inscription (request):
    return render(request, 'blog/Inscription.html')




def login (request):
    return render(request, 'blog/Login.html')


def logout (request):
    return render(request, 'blog/Accueil.html')

  #===================================== Chat views ================================
  
def generalchat(request):
        c = Chat.objects.all()
        documents = Document.objects.all() #file upload
        return render(request, "channels/Forum.html", {'generalchat': 'active', 'chat': c, 'documents': documents})

  
def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        time = datetime.now()
        c = Chat(user=request.user, message=msg, created=time)

        c = Chat(user=request.user, message=msg)

        if msg != '':            
           c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username})
    else:
       return HttpResponse('Request must be POST.')
   


def uploads(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum')
    else:
       form = DocumentForm()
       return render(request, 'channels/uploads.html', {
    'form': form
    })

  #============================= Login and register views =========================
 
def signup(request):
    # if request.user.is_authenticated:
    #     return redirect('blog:signin', username=request.user.username)
 
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
 
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('/blog/accueill')
 
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'blog/Login.html')
 
 
def signin(request):
    auth.logout(request)
    return redirect('/blog/accueil')
   
 
 
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return redirect('/blog/login')
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'blog/Inscription.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



def add_email (request):   
    email= Email.objects.all()
    if request.method == 'POST':
        email= Email(
            name = request.POST.get("name"),
            degree = request.POST.get("degree"),
            Subject = request.POST.get("Subject"),  
            message = request.POST.get("message"),           
        )
        email.save()
        return HttpResponseRedirect('email_detail')
    else:
        message ="Echec"
    return render(request,'blog/Contact.html',{'email':email})

# def oneemaildep(request, id):
#     email= Email.objects.get(pk=id)
#     return render(request, 'blog/Deletemail.html', {'email':email})

# def deletemail(request,id):
#     email= Email.objects.get(pk=id)
#     email.delete()
#     return HttpResponseRedirect('email_detail')
    



def forum (request):
    return render(request, 'blog/Forum.html')

def dashboard (request):
    intervention= Intervention.objects.all()
    chartObj = FusionCharts( 'pie3d', 'ex1', '1000', '400', 'chart-1', 'jsonurl', "/static/data/data.json")
   
    return render(request, 'blog/Tableau_de_Bord.html', {'intervention':intervention, 'output': chartObj.render()})


   #===========================================================================
   
   
def listservice (request):
    bureau = Bureau.objects.all()
    return render(request, 'blog/Services.html')

def listparc (request):
    return render(request, 'blog/Parcs.html')

def listintervention (request):
    return render(request, 'blog/Interventi.html')

    #============================== Chat views==================================
    
