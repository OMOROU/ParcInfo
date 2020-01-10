from django.urls import path
from django.contrib.auth.decorators import login_required
from django.http import *
from django.views.generic import TemplateView
from django.conf import settings


from . import views as userprofile

app_name="userprofile"
urlpatterns = [
    path('', userprofile.index, name='index'),
    
    #path('signup', userprofile.signup, name='signup'),
    
    path('loginView', userprofile.loginView, name='loginView'),
    path('logoutView', userprofile.logoutView, name='logoutView'),
    #path(r'^backoffice/$', TemplateView.as_view(template_name='backoffice/accueil.html'), name='accueil'),

    
    ]
