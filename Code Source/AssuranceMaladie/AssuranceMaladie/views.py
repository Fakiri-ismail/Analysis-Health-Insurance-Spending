from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Assurance
from . import ConnSQl

def home(request):
    return render(request,"pages/index.html")

def about(request):
    return render(request,"pages/about.html")

@login_required(login_url="/login/")
def listAssurance(request):
    listes=ConnSQl.listAssurance()
    return render(request, "assurance/listAssurance.html",{'listes':listes})

@login_required(login_url="/login/")
def assurance_details(request, id):
    assu=Assurance()
    assu=ConnSQl.getAssuranceByID(id)
    return render(request, "assurance/assurance_details.html",{'assu':assu})

@login_required(login_url="/login/")
def new_assurance(request):
    sel=Assurance()
    sel.allville=ConnSQl.allSelections()[0]
    sel.allNatAs=ConnSQl.allSelections()[1]
    sel.allSp=ConnSQl.allSelections()[2]
    sel.allQua=ConnSQl.allSelections()[3]
    sel.allPres=ConnSQl.allSelections()[4]
    sel.allMan=ConnSQl.allSelections()[5]
    if request.method=='POST':
        assu=Assurance()
        assu.ville=request.POST['ville']
        assu.natureAssurance=request.POST['natureAssurance']
        assu.specialiteExecute=request.POST['specialiteExecute']
        assu.manierExecuter=request.POST['manierExecuter']
        assu.prestation=request.POST['prestation']
        assu.qualiteBenificiaire=request.POST['qualiteBenificiaire']
        assu.tauxRemb=request.POST['tauxRemb']
        assu.baseRemb=request.POST['baseRemb']
        assu.dateRemb=request.POST['dateRemb']
        ConnSQl.insertToDB(assu.natureAssurance,assu.specialiteExecute,assu.manierExecuter,assu.prestation,assu.qualiteBenificiaire,assu.ville,assu.tauxRemb,assu.baseRemb,assu.dateRemb)
        return redirect("/listAssurance/")
    return render(request, "assurance/new_assurance.html",{"sel":sel})

@login_required(login_url="/login/")
def edit_assurance(request,id):
    sel=assu=Assurance()
    assu=ConnSQl.getAssuranceByID(id)
    sel.allville=ConnSQl.allSelections()[0]
    sel.allNatAs=ConnSQl.allSelections()[1]
    sel.allSp=ConnSQl.allSelections()[2]
    sel.allQua=ConnSQl.allSelections()[3]
    sel.allPres=ConnSQl.allSelections()[4]
    sel.allMan=ConnSQl.allSelections()[5]
    if request.method=='POST':
        assu=Assurance()
        v=assu.ville=request.POST['ville']
        nat=assu.natureAssurance=request.POST['natureAssurance']
        sp=assu.specialiteExecute=request.POST['specialiteExecute']
        mod=assu.manierExecuter=request.POST['manierExecuter']
        pre=assu.prestation=request.POST['prestation']
        ql=assu.qualiteBenificiaire=request.POST['qualiteBenificiaire']
        tr=assu.tauxRemb=request.POST['tauxRemb']
        br=assu.baseRemb=request.POST['baseRemb']
        dateR=assu.dateRemb=request.POST['dateRemb']
        ConnSQl.ModierAssur(id,v,nat,sp,mod,pre,ql,tr,br,dateR)
        return redirect("/listAssurance/")
    return render(request, "assurance/edit_assurance.html",{"assu":assu,"sel":sel})

@login_required(login_url="/login/")
def delete_assurance(request,id):
    assu=ConnSQl.getAssuranceByID(id)
    if request.method=='POST':
        # assurance_to_archive=Assurance.objects.filter(pk=assu.id)
        # assurance_to_archive.update(archive=True)
        # assu.delete()
        ConnSQl.SupprimerAssur(id)
        return redirect("/listAssurance/")
    return render(request, "assurance/delete_assurance.html",{"assu":assu})