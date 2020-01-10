from django.forms import ModelForm, Textarea
from django import forms
from .models import Departement, Bureau, Intervenant


class DepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = ('libelle_dep', 'description')
    
    # def clean_libelle_dep(self):
    #       libelle_dep = self.cleaned_data['libelle_dep']
    #       if self.instance.id:
    #          if Departement.objects.filter(libelle_dep=libelle_dep).exclude(id=self.instance.id):
    #             raise forms.ValidationError(
    #                         'Menu with this title already exists.')
    #          else:
    #             if Departement.objects.filter(libelle_dep=libelle_dep):
    #                raise forms.ValidationError(
    #                         'Menu with this subject already exists.')
    #             return libelle_dep

    # def clean_description(self):
    #       description = self.cleaned_data['description']
    #       if len(description) > 80:
    #          raise forms.ValidationError(
    #                         'content should not exceed 80 characters')
    #       return description
       

        

class BureauForm(ModelForm):
    num_bureau = forms.IntegerField()
    departement = forms.ModelChoiceField(queryset=Departement.objects.all(), initial=0)
    class Meta:
        model = Bureau
        fields = ('num_bureau', 'departement')
        
        
        
        
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['departement'].queryset = Departement.objects.none()

    #     if 'departement' in self.data:
    #         try:
                
    #           departement_id = int(self.data.get('departement'))
    #           self.fields['departement'].queryset = Departement.objects.filter(departement_id=departement_id).order_by('name')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['departement'].queryset = self.instance.departement.departement_set.order_by('name')
        
 

class IntervenantForm(ModelForm):
    class Meta:
        model = Intervenant
        fields = ('nom_intervenant', 'telephone', 'email')
       
            