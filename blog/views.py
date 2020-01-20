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
from .forms import EmailForm, ChatForm,  forms

from .models import Article
# from asgiref.sync import async_to_sync
# from channels.generic.chat import WebsocketConsumer
import json
# from chat.core.models.user import User
#from chat.core.models.message import Message


# class ChatConsumer(WebsocketConsumer):

#     def init_chat(self, data):
#         username = data['username']
#         user, created = User.objects.get_or_create(username=username)
#         content = {
#             'command': 'init_chat'
#         }
#         if not user:
#             content['error'] = 'Unable to get or create User with username: ' + username
#             self.send_message(content)
#         content['success'] = 'Chatting in with success with username: ' + username
#         self.send_message(content)

#     def fetch_messages(self, data):
#         messages = Message.last_50_messages()
#         content = {
#             'command': 'messages',
#             'messages': self.messages_to_json(messages)
#         }
#         self.send_message(content)

#     def new_message(self, data):
#         author = data['from']
#         text = data['text']
#         author_user, created = User.objects.get_or_create(username=author)
#         message = Message.objects.create(author=author_user, content=text)
#         content = {
#             'command': 'new_message',
#             'message': self.message_to_json(message)
#         }
#         self.send_chat_message(content)

#     def messages_to_json(self, messages):
#         result = []
#         for message in messages:
#             result.append(self.message_to_json(message))
#         return result

#     def message_to_json(self, message):
#         return {
#             'id': str(message.id),
#             'author': message.author.username,
#             'content': message.content,
#             'created_at': str(message.created_at)
#         }

#     commands = {
#         'init_chat': init_chat,
#         'fetch_messages': fetch_messages,
#         'new_message': new_message
#     }

#     def connect(self):
#         self.room_name = 'room'
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )
#         self.accept()

#     def disconnect(self, close_code):
#         # leave group room
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     def receive(self, text_data):
#         data = json.loads(text_data)
#         self.commands[data['command']](self, data)

#     def send_message(self, message):
#         self.send(text_data=json.dumps(message))

#     def send_chat_message(self, message):
#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#         # Send message to WebSocket
#         self.send(text_data=json.dumps(message))
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
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'blog/Inscription.html', {'form': f})


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
    
