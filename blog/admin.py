from django.contrib import admin
from blog.models import Article, Contact, Email, Message, Chat, UserProfileInfo

# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Email)
#admin.site.register(User)
admin.site.register(Message)
admin.site.register(Chat)
admin.site.register(UserProfileInfo)
