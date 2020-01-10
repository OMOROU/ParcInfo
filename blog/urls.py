from django.urls import path


from . import views as blog

app_name="blog"
urlpatterns = [
    path('index', blog.index, name='index'),
    path('contact', blog.contact, name='contact'),
    path('accueil', blog.accueil, name='accueil'),
    path('forum', blog.forum, name='forum'),
    path('signup', blog.signup, name='signup'),
    path('dashboard', blog.dashboard, name='dashboard'),
    path('login', blog.login, name='login'),
    path('lock', blog.lock, name='lock'),
    path('inscription', blog.inscription, name='inscription'),
    path('email_detail', blog.email_detail, name='email_detail'),
    #path('contactview', blog.contactview, name='contactview'),
    
    path('listservice', blog.listservice, name='listservice'),
    path('listparc', blog.listparc, name='listparc'),
    path('listintervention', blog.listintervention, name='listintervention'),
    
    path('add_email', blog.add_email, name='add_email'),
  
    #path('successview/', blog.successview, name='successview'),
    
    ]
