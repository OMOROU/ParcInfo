from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


# LIBELLE_DEPARTEMENT= (
#     ('COMPTABILITE', 'COMPTABILITE'),
#     ('COMMUNICATION', 'COMMUNICATION'),
#     ('INFORMATIQUE', 'INFORMATIQUE'),
#     ('MARKETING', 'MARKETING'),
#     ('RESEAUX', 'RESEAUX'),
    
# ) 


class Departement(models.Model):
    libelle_dep = models.CharField("Libelle du departement", max_length=100, blank=True, null=True)
    description = models.CharField("Description du Departement",max_length=100, blank=True, null=True)
    
    
    class Meta:
        verbose_name = _("Departement")
        verbose_name_plural = _("Departements")
        
    def __str__(self):
        return '%s' % self.libelle_dep

    def get_absolute_url(self):
        return reverse("departement_detail",kwargs={"pk": self.pk})
    


class Bureau(models.Model):
    num_bureau = models.IntegerField(("numéro du Bureau"), blank=True, null=True)
    departement = models.ForeignKey(Departement, related_name='departement', on_delete=models.CASCADE, blank=True, null=True)
    
    
    class Meta:
        verbose_name = _("Bureau")
        verbose_name_plural = _("Bureaux")
        
    def __str__(self):
        return '%s' % self.num_bureau

    def get_absolute_url(self):
        return reverse("bureau_detail",kwargs={"pk": self.pk})
    



class Intervenant(models.Model):
    nom_intervenant =  models.CharField("nom de l'intervenant", max_length=100, blank=True, null=True )
    telephone = models.CharField("telephone", max_length=11, blank=True, null=True)
    email= models.EmailField(_("couriel"), blank=True, null=True)
    

    class Meta:
        verbose_name = _("Intervenant")
        verbose_name_plural = _("Intervenants")

    def __str__(self):
        return  self.nom_intervenant

    def get_absolute_url(self):
        return reverse("intervenant_detail", kwargs={"pk": self.pk})

        

