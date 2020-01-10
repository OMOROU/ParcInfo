from django.urls import path

from . import views as intervention

app_name="intervention"
urlpatterns = [
         path('intervention', intervention.intervention, name='intervention'),
         path('add_intervention', intervention.add_intervention, name='add_intervention'),
         path('intervention_detail', intervention.intervention_detail, name='intervention_detail'),
         path('oneinterven/<int:id>', intervention.oneinterven, name='oneinterven'),
         path('updateinterven/<int:id>', intervention.updateinterven, name='updateinterven'),
         path('oneintervendel/<int:id>', intervention.oneintervendel, name='oneintervendel'),
         path('deleteinterven/<int:id>', intervention.deleteinterven, name='deleteinterven'),
         
         
         
         
         path('panne', intervention.panne, name='panne'),
         path('add_panne', intervention.add_panne, name='add_panne'),
         path('panne_detail', intervention.panne_detail, name='panne_detail'),
         path('onepanne/<int:id>', intervention.onepanne, name='onepanne'),
         path('updatepan/<int:id>', intervention.updatepan, name='updatepan'),
         path('onepannedel/<int:id>', intervention.onepannedel, name='onepannedel'),
         path('deletepan/<int:id>', intervention.deletepan, name='deletepan'),
         
         
         
         path('type_panne', intervention.type_panne, name='type_panne'),
         path('add_type_panne', intervention.add_type_panne, name='add_type_panne'),
         path('type_panne_detail', intervention.type_panne_detail, name='type_panne_detail'),
         path('onetypepan/<int:id>', intervention.onetypepan, name='onetypepan'),
         path('updatetypepan/<int:id>', intervention.updatetypepan, name='updatetypepan'),
         path('onetypepandel/<int:id>', intervention.onetypepandel, name='onetypepandel'),
         path('deletetypepan/<int:id>', intervention.deletetypepan, name='deletetypepan'),
        
        
]