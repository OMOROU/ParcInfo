import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from parc.models import Materiel
from intervention.models import Intervention, Panne
from service.models import Bureau, Departement, Intervenant

from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone



#Create your models here.

class Article(models.Model):
    name = models.CharField(("nom de l'articles"), max_length=100, blank=True, null=True)
   

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
    
class Contact(models.Model):
    email = models.EmailField(("Email"), max_length=100, blank=True, null=True)
    creatdate = models.DateField(_("Date d'envoie"))
   

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("contact_detail", kwargs={"pk": self.pk})
    
class Email(models.Model):
    name = models.CharField(("Full name "), max_length=100, blank=True, null=True)
    Subject = models.CharField(("Prenom "), max_length=100, blank=True, null=True)
    message = models.CharField(("nom "), max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")

    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse("email_detail", kwargs={"pk": self.pk})
    
    
      #============================= Midels de chat ==================================
      
# @python_2_unicode_compatible
# class User(AbstractUser):

#     last_read_date = models.DateTimeField(
#         auto_now_add=True,
#         blank=False,
#         null=False
#     )
#     online = models.BooleanField(null=False, blank=False, default=False)

#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.username

#     def read(self):
#         self.last_read_date = timezone.now()
#         self.save()

#     def unread_messages(self):
#         return Message.objects.filter(created_at__gt=self.last_read_date) \
#                               .count()
      
      
      
def validate_message_content(content):
    if content is None or content == "" or content.isspace():
        raise ValidationError(
            'Content is empty/invalid',
            code='invalid',
            params={'content': content},
        )


class Message(models.Model):

    id = models.UUIDField(
        primary_key=True,
        null=False,
        default=uuid.uuid4,
        editable=False
    )
    # author = models.ForeignKey(
    #     'User',
    #     blank=False,
    #     null=False,
    #     related_name='author_messages',
    #     on_delete=models.CASCADE
    # )
    content = models.TextField(validators=[validate_message_content])
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def last_50_messages():
        return Message.objects.order_by('-created_at').all()[:50]