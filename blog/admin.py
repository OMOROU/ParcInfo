from django.contrib import admin
from blog.models import Article, Contact, Email, Message

# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Email)
#admin.site.register(User)
admin.site.register(Message)