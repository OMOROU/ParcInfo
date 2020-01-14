from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from intervention.models import Panne, Type_panne, Intervention
from service.models import  Intervenant
from parc.models import Materiel
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from datetime import datetime


# Create your views here.
def intervention (request):
    intervention= Intervention.objects.all()
    pannes = Panne.objects.all()
    intervenants = Intervenant.objects.all()
   
    return render(request, 'intervention/Intervention.html', {'pannes':pannes, 'intervenants':intervenants})


def intervention_detail (request):
    intervention= Intervention.objects.all()
    pannes = Panne.objects.all()
    intervenant = Intervention.objects.all()
   
    return render(request, 'intervention/Intervention_detail.html', {'intervention':intervention})

     #============================== View add de intervention ===================================

def add_intervention(request):
    intervention= Intervention.objects.all()
    panne = Panne.objects.get(libelle_pan=request.POST.get("panne"))
    intervenant = Intervenant.objects.get(nom_intervenant=request.POST.get("intervenant"))
    
    
    if request.method == 'POST':
        intervention = Intervention(
            libelle_interv = request.POST.get("libelle_interv"),
            date_interv = request.POST.get("date_interv"),
            accomplie = request.POST.get("accomplie"),
            type_interv = request.POST.get("type_interv"),
            consigne = request.POST.get("consigne"),  
            intervenant = intervenant,
            panne = panne,
            
                      
        )
        intervention.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('intervention_detail')
    else:
        mssage ="Echec"
    return render(request,'intervention/Intervention.html',{'intervention':intervention})

     
     #======================== View Update et Delete de intervention ===========================
     
def oneinterven(request, id):
    intervention = Intervention.objects.get(pk=id)
    pannes = Panne.objects.all()
    intervenants = Intervenant.objects.all()
   
    return render(request, 'intervention/Updateinterven.html', {'intervention':intervention, 'pannes':pannes, 'intervenants':intervenants})


def updateinterven(request, id):
    intervention = Intervention.objects.get(pk=id)
    panne = Panne.objects.get(libelle_pan=request.POST.get("panne"))
    intervenant = Intervenant.objects.get(nom_intervenant=request.POST.get("intervenant"))
    
    if request.method == 'POST':
        intervention = Intervention(
            id = id, 
            libelle_interv = request.POST.get("libelle_interv"),
            date_interv = request.POST.get("date_interv"),
            accomplie = request.POST.get("accomplie"),
            type_interv = request.POST.get("type_interv"),
            consigne = request.POST.get("consigne"),  
            intervenant = intervenant,
            panne = panne,
            
                      
        )
        intervention.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('/intervention/intervention_detail')
    

def oneintervendel(request, id):
    intervention = Intervention.objects.get(pk=id)
    pannes = Panne.objects.all()
    intervenants = Intervenant.objects.all()
   
    return render(request, 'intervention/Deleteinterven.html', {'intervention':intervention, 'pannes':pannes, 'intervenants':intervenants})


def deleteinterven(request, id):
    intervention = Intervention.objects.get(pk=id)
    intervention.delete()
    return HttpResponseRedirect('/intervention/intervention_detail')
    


    

#==============================================Views de Panne===========================================
def panne (request):
    type_pannes = Type_panne.objects.all()
    intervenants = Intervenant.objects.all()
    materiels = Materiel.objects.all()
    
    
    return render(request, 'intervention/Panne.html', {'type_pannes':type_pannes, 'intervenants':intervenants, 'materiels':materiels})

    #=================================== View detail de panne =================================

def panne_detail (request):
    panne= Panne.objects.all()
    type_pannes = Type_panne.objects.all()
    intervenants = Intervenant.objects.all()
    materiels = Materiel.objects.all()
    
    
    return render(request, 'intervention/Panne_detail.html', {'panne':panne})

      #=================================== View add de panne =================================
      
def add_panne(request):
    panne= Panne.objects.all()
    type_panne = Type_panne.objects.get(libelle_pan=request.POST.get("type_panne"))
    intervenant = Intervenant.objects.get(nom_intervenant=request.POST.get("intervenant"))
    materiel = Materiel.objects.get(name=request.POST.get("materiel") )
    if request.method == 'POST':
        panne = Panne(
            libelle_pan = request.POST.get("libelle_pan"),
            description = request.POST.get("description"),
            niveau = request.POST.get("niveau"),
            type_panne = type_panne,
            intervenant = intervenant,
            materiel = materiel,
                      
        )
        panne.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('panne_detail')
    else:
        mssage ="Echec"
    return render(request,'intervention/Panne.html',{'panne':panne})

    
      #================================ View Update et Delete de panne =======================
      
def onepanne(request, id):
    panne = Panne.objects.get(pk=id)
    type_pannes = Type_panne.objects.all()
    intervenants = Intervenant.objects.all()
    materiels = Materiel.objects.all()
    
    return render(request, 'intervention/UpdatePan.html', {'panne':panne, 'type_pannes':type_pannes, 'intervenants':intervenants, 'materiels':materiels})


def updatepan(request, id):
    panne = Panne.objects.get(pk=id)
    type_panne = Type_panne.objects.get(libelle_pan=request.POST.get("type_panne"))
    intervenant = Intervenant.objects.get(nom_intervenant=request.POST.get("intervenant"))
    materiel = Materiel.objects.get(name=request.POST.get("materiel") )
    if request.method == 'POST':
        panne = Panne(
            id = id,
            libelle_pan = request.POST.get("libelle_pan"),
            description = request.POST.get("description"),
            niveau = request.POST.get("niveau"),
            type_panne = type_panne,
            intervenant = intervenant,
            materiel = materiel,
                      
        )
        panne.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('/intervention/panne_detail')
    
    
def onepannedel(request, id):
    panne = Panne.objects.get(pk=id)
    type_pannes = Type_panne.objects.all()
    intervenants = Intervenant.objects.all()
    materiels = Materiel.objects.all()
    
    return render(request, 'intervention/DeletePan.html', {'panne':panne, 'type_pannes':type_pannes, 'intervenants':intervenants, 'materiels':materiels})


def deletepan(request, id):
    panne = Panne.objects.get(pk=id)
    panne.delete()
    return HttpResponseRedirect('/intervention/panne_detail')
    


    

#==============================================Views de type de panne================================
def type_panne (request):
    
    return render(request, 'intervention/Type_panne.html')

    #=================================== View detail de type panne =================================
def type_panne_detail (request):
    type_panne = Type_panne.objects.all()
    
    return render(request, 'intervention/Type_panne_detail.html',{'type_panne':type_panne})

    #=================================== View add de type panne ====================================

def add_type_panne(request):
    type_panne= Type_panne.objects.all()
    if request.method == 'POST':
        type_panne = Type_panne(
            libelle_pan = request.POST.get("libelle_pan"),
            description = request.POST.get("description"),
                      
        )
        type_panne.save()
        return HttpResponseRedirect('type_panne_detail')
    else:
        mssage ="Echec"
    return render(request,'intervention/Type_panne.html',{'type_panne':type_panne})

    #=================================== View Update et Delete de type panne ======================
    
def onetypepan(request, id):
    type_panne = Type_panne.objects.get(pk=id)
    
    return render(request, 'intervention/UpdateTypepan.html',{'type_panne':type_panne})


def updatetypepan(request, id):
    type_panne = Type_panne.objects.get(pk=id)
    if request.method == 'POST':
        type_panne = Type_panne(
            id = id,
            libelle_pan = request.POST.get("libelle_pan"),
            description = request.POST.get("description"),
                      
        )
        type_panne.save()
        return HttpResponseRedirect('/intervention/type_panne_detail')
    
    
def onetypepandel(request, id):
    type_panne = Type_panne.objects.get(pk=id)
    
    return render(request, 'intervention/DeleteTypepan.html',{'type_panne':type_panne})

def deletetypepan(request, id):
    type_panne = Type_panne.objects.get(pk=id)
    type_panne.delete()
    return HttpResponseRedirect('/intervention/type_panne_detail')
    

#==============================================Views end====================================================