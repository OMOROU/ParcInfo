from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from .forms import IntervenantForm, DepartementForm, BureauForm, forms
from .models import Bureau, Departement, Intervenant
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse

# Create your views here.

def departement (request):
    return render(request, 'service/Departement.html')
        #==============================View de detail===============================

def departement_detail(request):
    departement= Departement.objects.all()
    
    return render(request, 'service/Departement_detail.html', {'departement':departement})

        #====================================La view form departemet================
def add_departement (request):   
    departement= Departement.objects.all()
    if request.method == 'POST':
        departement= Departement(
            libelle_dep = request.POST.get("libelle_dep"),
            description = request.POST.get("description"),            
        )
        departement.save()
        return HttpResponseRedirect('departement_detail')
    else:
        message ="Echec"
    return render(request,'service/Departement.html',{'departement':departement})


def onedep(request, id):
    departement = Departement.objects.get(pk=id)
    return render(request, "service/Updatedep.html", {'departement':departement})

def updatedep(request, id):
    departement = Departement.objects.get(pk=id)
    if request.method == 'POST':
        departement= Departement(
            id=id,           
            libelle_dep = request.POST.get("libelle_dep"),
            description = request.POST.get("description"),            
        )
        departement.save()
        return HttpResponseRedirect('/service/departement_detail')
    
def onedepdelete(request, id):
    departement = Departement.objects.get(pk=id)
    return render(request, "service/deletedep.html", {'departement':departement})

def deletedep(request,id):
    departement = Departement.objects.get(pk=id)
    departement.delete()
    return HttpResponseRedirect('/service/departement_detail')
    


#======================================view de bureau=======================================================

def bureau (request):
    departements = Departement.objects.all()
    
    #departement.pk = None
    return render(request, 'service/Bureau.html',{'departements':departements})
   
       #============================= View de deteil bureau ===========================

def bureau_detail (request):
    departements = Departement.objects.all()
    bureau  = Bureau.objects.all()
    print(bureau)
    
    return render(request, 'service/Bureau_detail.html', {'bureau':bureau})




       
       #============================= View form de  bureau ===========================
def add_bureau (request):
    bureau= Bureau.objects.all()
    departement = Departement.objects.get(libelle_dep=request.POST.get("departement"))
    if request.method == 'POST':
        bureau= Bureau(
            num_bureau = request.POST.get("num_bureau"),
            departement = departement,
                      
        )
        bureau.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('bureau_detail')
    else:
        mssage ="Echec"
    return render(request,'service/Bureau.html',{'bureau':bureau})

      #============================= View Update et Delete de  bureau ===================
      
def oneburo(request, id):
    bureau  = Bureau.objects.get(pk=id)
    departement = Departement.objects.all()
    
    return render(request, 'service/Updateburo.html', {'bureau':bureau, 'departement':departement})

def updateburo(request, id):
    bureau  = Bureau.objects.get(pk=id)
    departement = Departement.objects.get(libelle_dep=request.POST.get("departement"))
    if request.method == 'POST':
        bureau= Bureau(
            id=id,
            num_bureau = request.POST.get("num_bureau"),
            departement = departement,
                      
        )
        bureau.save()
       # mssage =  "% Bureau added succesfully"
        return HttpResponseRedirect('/service/bureau_detail')


def oneburodel(request, id):
    bureau  = Bureau.objects.get(pk=id)
    departement = Departement.objects.all()
    
    return render(request, 'service/Deleteburo.html', {'bureau':bureau, 'departement':departement})


def deleteburo(request, id):
    bureau  = Bureau.objects.get(pk=id)
    bureau.delete()
    return HttpResponseRedirect('/service/bureau_detail')
    

    

   

#=======================================La view form d'intervenant==========================================
def add_intervenant (request):
    intervenant= Intervenant.objects.all()
    if request.method == 'POST':
        intervenant = Intervenant(
            nom_intervenant = request.POST.get("nom_intervenant"),
            telephone = request.POST.get("telephone"),
            email = request.POST.get("email"),           
        )
        intervenant.save()
        return HttpResponseRedirect('intervenant_detail')
    else:
        mssage ="Echec"
    return render(request,'service/Intervenant.html',{'intervenant':intervenant})

    #=================================Le view d'intervenant==================================
def intervenant (request):
    
    
    return render(request, 'service/Intervenant.html')

    #=================================Le view detail intervenant==================================
def intervenant_detail (request):
    intervenant  = Intervenant.objects.all()
    
    
    return render(request, 'service/Intervenant_detail.html', {'intervenant':intervenant})

    #=================================Le view Udate et Delete intervenant==================================

def oneinterv(request, id):
    intervenant  = Intervenant.objects.get(pk=id)
    
    return render(request, 'service/Updateinterv.html', {'intervenant':intervenant})


def updateinterv(request, id):
    intervenant  = Intervenant.objects.get(pk=id)
    if request.method == 'POST':
        intervenant = Intervenant(
            id=id,
            nom_intervenant = request.POST.get("nom_intervenant"),
            telephone = request.POST.get("telephone"),
            email = request.POST.get("email"),           
        )
        intervenant.save()
        return HttpResponseRedirect('/service/intervenant_detail')
    

def oneintervdelete(request, id):    
    intervenant  = Intervenant.objects.get(pk=id)
    
    return render(request, 'service/Deleteinterv.html', {'intervenant':intervenant})

def deleteinterv(request,id):
    intervenant  = Intervenant.objects.get(pk=id)
    intervenant.delete()
    return HttpResponseRedirect('/service/intervenant_detail')
    





#==========================================END INTERVENANT =================================================

def page(request):
    return render(request, 'service/page.html')