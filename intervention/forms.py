from django.forms import ModelForm, Textarea
from intervention.models import Type_panne, Panne, Intervention
from django.contrib.admin import widgets

class Type_panneForm(ModelForm):
    class Meta:
        model = Type_panne
        fields = ('description', 'libelle_pan')
        


class PanneForm(ModelForm):
    class Meta:
        model = Panne
        fields = ('description', 'niveau', 'type_panne', 'intervenant', 'materiel')
        
        
  
class InterventionForm(ModelForm):
    date_interv = forms.DateTimeField(widget=widgets.AdminDateTimeWidget)
    class Meta:
        model = Intervention
        fields = ('libelle_interv', 'date_interv', 'accomplie', 'type_interv', 'consigne', 'intervenant', 'panne')
       
