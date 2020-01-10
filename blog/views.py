from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm 
from collections import OrderedDict
from blog.fusioncharts import FusionCharts
from django.views import generic
from service.models import Bureau, Intervenant
from intervention.models import Intervention, Panne
from .models import Email
from .forms import EmailForm, forms

from .models import Article

# Create your views here.

def index (request):
    
   
    return render(request, 'blog/Index.html')


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



def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponseRedirect('/blog/contact')
        else:  # sinon une erreur sera affichée
                error = True
        return  redirect('inscription')
    form = AuthenticationForm() 
    return render(request, 'blog/Login.html', {'form': form})



# def contactview(request):
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = form.cleaned_data['subject']
#             from_email = form.cleaned_data['from_email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('/blog/successview')
#     return render(request, "blog/Contact.html", {'form': form})

# def successview(request):
#     return HttpResponse('Success! Thank you for your message.')

def add_email (request):   
    email= Email.objects.all()
    if request.method == 'POST':
        email= Email(
            name = request.POST.get("name"),
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
