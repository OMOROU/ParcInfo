from django.contrib import admin
from blog.models import Article, Contact, Email

# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Email)