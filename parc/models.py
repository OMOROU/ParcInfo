from django.db import models
from django.utils.translation import gettext as _
from service.models import  Bureau
# Create your models here.

        
class Type_materiel(models.Model):
    libelle_materiel= models.CharField("libelle type_materiel", max_length=100, blank=True, null=True)
    description= models.CharField("Description", max_length=100, blank=True, null=True)
   

    class Meta:
        verbose_name = _("Type_materiel")
        verbose_name_plural = _("Types_materiels")

    def __str__(self):
        return '%s' % self.libelle_materiel

    def get_absolute_url(self):
        return reverse("type_materiel_detail", kwargs={"pk": self.pk})
            



class Materiel(models.Model):
    name = models.CharField("nom materiel",max_length=100, blank=True, null=True)
    numero_serie = models.CharField(_("numero_serie Materiel"), max_length=100, blank=True, null=True)
    caracteristique =  models.TextField("caracteristique", max_length=100, blank=True, null=True )
    bureau = models.ForeignKey(Bureau, related_name='bureau', on_delete=models.CASCADE, blank=True, null=True)
    type_materiel = models.ForeignKey(Type_materiel, related_name='type_materiel', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = _("Materiel")
        verbose_name_plural = _("Materiels")
        
    def __str__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return reverse("materiel_detail",kwargs={"pk": self.pk})
    



# LIBELLE_MATERIEL= (
#     ('ORDINATEUR', 'ORDINATEUR'),
#     ('IMPRIMANT', 'IMPRIMANT'),
#     ('SCANNER', 'SCANNER'),
#     ('PHOTOCOPIEUSE', 'PHOTOCOPIEUSE'),
#     ('PERIPHERIQUE', 'PERIPHERIQUE'),
#     ('MONITEUR', 'MONITEUR'),
# ) 





        
