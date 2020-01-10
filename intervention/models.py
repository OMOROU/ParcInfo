from django.db import models
from django.utils.translation import gettext as _
from service.models import Intervenant
from parc.models import Materiel
# Create your models here.

 

class Type_panne(models.Model):
    libelle_pan = models.CharField("libelle de la panne", max_length=100, blank=True, null=True)
    description = models.CharField("description type de panne",max_length=100, blank=True, null=True)
   
    
    class Meta:
        verbose_name = _("Type_panne")
        verbose_name_plural = _("Types_pannes")
        
    def __str__(self):
        return self.libelle_pan

    def get_absolute_url(self):
        return reverse("type_panne_detail",kwargs={"pk": self.pk})
    



class Panne(models.Model):
    libelle_pan = models.CharField("libelle de la panne", max_length=100, blank=True, null=True)
    description = models.CharField("description de la panne",max_length=100, blank=True, null=True)
    type_panne = models.ForeignKey(Type_panne, related_name='type_panne', on_delete=models.CASCADE, blank=True, null=True)
    intervenant =  models.ForeignKey(Intervenant, verbose_name='intervenant', on_delete=models.CASCADE, blank=True, null=True)
    materiel =  models.ForeignKey(Materiel, verbose_name='materiel', on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Panne")
        verbose_name_plural = _("Pannes")
        
    def __str__(self):
        return self.libelle_pan

    def get_absolute_url(self):
        return reverse("panne_detail",kwargs={"pk": self.pk})
    




TYPE_INTERVENTION = (
    ('EN PERSONNE', 'EN PERSONNE'),
    ('EN RESEAU', 'EN RESEAU'),
    
) 
    

    
class Intervention(models.Model):
    libelle_interv =  models.CharField("libelle de l'intervention",  max_length=100, blank=True, null=True)
    date_interv = models.DateField(("date de l'intervention"), blank=True, null=True)
    accomplie = models.BooleanField(("Statut de la panne"), blank=True, null=True)
    type_interv = models.CharField("type de l'intervention", max_length=100, choices =TYPE_INTERVENTION, default=[0])
    consigne =  models.CharField("consigne de la panne ", max_length=100, blank=True, null=True )
    intervenant =  models.ForeignKey(Intervenant, verbose_name='intervenant', on_delete=models.CASCADE, blank=True, null=True)
    panne =  models.ForeignKey(Panne, verbose_name='panne', on_delete=models.CASCADE, blank=True, null=True)
    

    
    

    class Meta:
        verbose_name = _("Intervention")
        verbose_name_plural = _("Interventions")

    def str(self):
        try:
            libelle_interv = self.libelle_interv
        except :
            libelle_interv = 'No name'
        return f'{libelle_interv}'
    
    def get_absolute_url(self):
        return reverse("intervention_detail", kwargs={"pk": self.pk})

        




