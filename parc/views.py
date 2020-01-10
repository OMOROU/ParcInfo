from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Materiel, Type_materiel
from service.models import  Bureau
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

# Create your views here.
def materiel (request):
    bureaux = Bureau.objects.all()
    type_materiels  = Type_materiel.objects.all()
    
    return render(request, 'parc/index.html', {'bureaux':bureaux, 'type_materiels':type_materiels})
          #============================View detail de materiel=======================

def materiel_detail (request):
    bureaux = Bureau.objects.all()
    type_materiels  = Type_materiel.objects.all()
    materiel = Materiel.objects.all()
    print("materiel")
    
    return render(request, 'parc/Materiel_detail.html', {'materiel':materiel})

           #============================ View save de materiel =======================
           
def add_materiel(request):
    materiel= Materiel.objects.all()
    bureau = Bureau.objects.get(num_bureau=request.POST.get("bureau"))
    types_materiel = Type_materiel.objects.get(libelle_materiel=request.POST.get("type_materiel"))
    if request.method == 'POST':
        materiel= Materiel(
            name = request.POST.get("name"),
            numero_serie = request.POST.get("numero_serie"),
            caracteristique = request.POST.get("caracteristique"),
            bureau = bureau,
            type_materiel = types_materiel,
                      
        )
        materiel.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('materiel_detail')
    else:
        mssage ="Echec"
    return render(request,'parc/Materiel.html',{'materiel':materiel})

        #============================ View Update et Delete de materiel ========================
        
def onemateriel(request, id):
    materiel = Materiel.objects.get(pk=id)
    bureaux = Bureau.objects.all()
    type_materiels = Type_materiel.objects.all()
    
    return render(request, 'parc/UpdateMate.html', { 'materiel':materiel, 'bureaux':bureaux, 'type_materiels':type_materiels})


def updatemate(request, id):
    materiel = Materiel.objects.get(pk=id)
    bureau = Bureau.objects.get(num_bureau=request.POST.get("bureau"))
    types_materiel = Type_materiel.objects.get(libelle_materiel=request.POST.get("type_materiel"))
    if request.method == 'POST':
        materiel= Materiel(
            id = id,
            name = request.POST.get("name"),
            numero_serie = request.POST.get("numero_serie"),
            caracteristique = request.POST.get("caracteristique"),
            bureau = bureau,
            type_materiel = types_materiel,
                      
        )
        materiel.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('/parc/materiel_detail')
    
def onematerieldel(request, id):
    materiel = Materiel.objects.get(pk=id)
    bureaux = Bureau.objects.all()
    type_materiels = Type_materiel.objects.all()
    
    return render(request, 'parc/DeleteMate.html', { 'materiel':materiel, 'bureaux':bureaux, 'type_materiels':type_materiels})


def deletemate(request, id):
    materiel = Materiel.objects.get(pk=id)
    materiel.delete()
    return HttpResponseRedirect('/parc/materiel_detail')
    






#=========================================Views de type de materiel===================================

def types_materiel (request):
    
    return render(request, 'parc/Types_materiel.html')

     #============================ View detail de types materiel ====================================

def types_materiel_detail (request):
    types_materiel  = Type_materiel.objects.all()
    
    return render(request, 'parc/Type_materiel_detail.html', {'types_materiel':types_materiel})

       #=============================== Views add de type materiel=============================

def add_types_materiel(request):
    types_materiel = Type_materiel.objects.all()
    if request.method == 'POST':
        types_materiel = Type_materiel(
            libelle_materiel = request.POST.get("libelle_materiel"),
            description = request.POST.get("description"),
                      
        )
        types_materiel.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('types_materiel_detail')
    else:
        mssage ="Echec"
    return render(request,'service/Types_materiel.html',{'types_materiel':types_materiel})

        #============================== Views Update et Delete de type materiel=================

def onetypemater(request, id):
    types_materiel = Type_materiel.objects.get(pk=id)
    
    return render(request, 'parc/UpdateTypeMate.html', {'types_materiel':types_materiel})

def updatetypemate(request, id):
    types_materiel = Type_materiel.objects.get(pk=id)
    if request.method == 'POST':
        types_materiel = Type_materiel(
            id = id, 
            libelle_materiel = request.POST.get("libelle_materiel"),
            description = request.POST.get("description"),
                      
        )
        types_materiel.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('/parc/types_materiel_detail')


def onetypematerdel(request, id):
    types_materiel = Type_materiel.objects.get(pk=id)
    
    return render(request, 'parc/DeleteTypeMate.html', {'types_materiel':types_materiel})


def deletetypemate(request, id):
    types_materiel = Type_materiel.objects.get(pk=id)
    types_materiel.delete()
    return HttpResponseRedirect('/parc/types_materiel_detail')
    

    


#========================================== END =======================================================

