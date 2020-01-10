from django.contrib import admin
from intervention.models import Panne, Type_panne, Intervention

# Register your models here.
admin.site.register(Panne)
admin.site.register(Type_panne)
admin.site.register(Intervention)