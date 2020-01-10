from django.db import models
from django.utils.translation import gettext as _
from parc.models import Materiel
from intervention.models import Intervention, Panne
from service.models import Bureau, Departement, Intervenant

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
    
    
