from django.urls import path

from . import views as service

app_name="service"
urlpatterns = [
         
         path('bureau', service.bureau, name='bureau'), 
         path('bureau_detail', service.bureau_detail, name='bureau_detail'), 
         path('add_bureau', service.add_bureau, name='add_bureau'),   
         path('oneburo/<int:id>', service.oneburo, name='oneburo'), 
         path('updateburo/<int:id>', service.updateburo, name='updateburo'),
         path('oneburodel/<int:id>', service.oneburodel, name='oneburodel'), 
         path('deleteburo/<int:id>', service.deleteburo, name='deleteburo'), 
         
        
         
         path('departement', service.departement, name='departement'),
         path('departement_detail', service.departement_detail, name='departement_detail'),      
         path('add_departement', service.add_departement, name='add_departement'), 
         path('onedep/<int:id>', service.onedep, name='onedep'), 
         path('updatedep/<int:id>', service.updatedep, name='updatedep'), 
         path('onedepdelete/<int:id>', service.onedepdelete, name='onedepdelete'), 
         path('deletedep/<int:id>', service.deletedep, name='deletedep'), 
         
         
         path('oneinterv/<int:id>', service.oneinterv, name='oneinterv'), 
         path('updateinterv/<int:id>', service.updateinterv, name='updateinterv'),
         path('oneintervdelete/<int:id>', service.oneintervdelete, name='oneintervdelete'), 
         path('deleteinterv/<int:id>', service.deleteinterv, name='deleteinterv'), 
         path('add_intervenant', service.add_intervenant, name='add_intervenant'),   
         path('intervenant', service.intervenant, name='intervenant'),
         path('intervenant_detail', service.intervenant_detail, name='intervenant_detail'),
         path('page', service.page, name='page'), 
        
]