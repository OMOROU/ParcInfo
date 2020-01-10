from django.urls import path

from . import views as parc 

app_name="parc"
urlpatterns = [
         path('add_materiel', parc.add_materiel, name='add_materiel'),
         path('materiel', parc.materiel, name='materiel'),
         path('materiel_detail', parc.materiel_detail, name='materiel_detail'),
         path('onemateriel/<int:id>', parc.onemateriel, name='onemateriel'), 
         path('updatemate/<int:id>', parc.updatemate, name='updatemate'),
         path('onematerieldel/<int:id>', parc.onematerieldel, name='onematerieldel'), 
         path('deletemate/<int:id>', parc.deletemate, name='deletemate'),
         
         
         
         path('add_types_materiel', parc.add_types_materiel, name='add_types_materiel'),
         path('types_materiel', parc.types_materiel, name='types_materiel'),
         path('types_materiel_detail', parc.types_materiel_detail, name='types_materiel_detail'),
         path('onetypemater/<int:id>', parc.onetypemater, name='onetypemater'), 
         path('updatetypemate/<int:id>', parc.updatetypemate, name='updatetypemate'),
         path('onetypematerdel/<int:id>', parc.onetypematerdel, name='onetypematerdel'), 
         path('deletetypemate/<int:id>', parc.deletetypemate, name='deletetypemate'),
        
]