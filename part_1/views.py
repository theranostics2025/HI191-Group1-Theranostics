from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.urls import reverse
from . forms import *
from part_2.forms import *
from . models import *
from part_2.models import *
from part_3.models import *
from part_3.forms import *
from part_4.forms import *
from part_4.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test as userPassesTest

def isSuperuser(user):
    return user.is_superuser

def homePage(request):
    return render(request, 'part_1/home-page.html')

@userPassesTest(isSuperuser)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('patientList')
    else:
        form = UserCreationForm()
    return render(request, 'part_1/register-user.html', {'form' : form})

@login_required
def patientList(request):
    patients = Patient.objects.all()
    low_risk = request.GET.get('flexCheckLowRisk')
    intermediate_risk = request.GET.get('flexCheckIntermediateRisk')
    high_risk = request.GET.get('flexCheckHighRisk')
    bone_metastasis = request.GET.get('flexCheckMetastasis')
    side_effects = request.GET.get('flexCheckSideEffect')
    #Screening fields
    prostateLS = request.GET.get('flexCheckProstateL')
    nodeLS = request.GET.get('flexCheckLNL')
    boneLS = request.GET.get('flexCheckBoneL')
    brainLS = request.GET.get('flexCheckBrainL')
    lungLS = request.GET.get('flexCheckLungL')
    liverLS = request.GET.get('flexCheckLiverL')
    #Post-therapy fields
    prostateLPT = request.GET.get('flexCheckProstateLPT')
    nodeLPT = request.GET.get('flexCheckLNLPT')
    boneLPT = request.GET.get('flexCheckBoneLPT')
    lungLPT = request.GET.get('flexCheckLungLPT')
    liverLPT = request.GET.get('flexCheckLiverLPT')
    #Follow-up fields
    prostateLFU = request.GET.get('flexCheckProstateLFU')
    nodeLFU = request.GET.get('flexCheckLNLFU')
    boneLFU = request.GET.get('flexCheckBoneLFU')
    brainLFU = request.GET.get('flexCheckBrainLFU')
    lungLFU = request.GET.get('flexCheckLungLFU')
    liverLFU = request.GET.get('flexCheckLiverLFU')


    #Risk Assessment
    if low_risk == 'on':
        if intermediate_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')
        elif high_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk')
        else:
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk')

    if intermediate_risk == 'on':
        if low_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')
        elif high_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk')
        else:
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')

    if high_risk == 'on':
        if low_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk')
        elif intermediate_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')
        else:
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk')
    
    #Bone Metastasis
    if bone_metastasis == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__bone_metastasis_status = 'Metastasis')

    #Side Effect
    if side_effects == 'on':
        patients = Patient.objects.prefetch_related('t_patient').filter(t_patient__side_effects__isnull=False)

    #Screening Filters
    if prostateLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_prostate_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_prostate_lesion_status__exact= 'Present')

    if nodeLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_lymph_node_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_lymph_node_lesion_status__exact= 'Present')
    
    if boneLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_bone_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_bone_lesion_status__exact= 'Present')

    if brainLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_brain_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_brain_lesion_status__exact= 'Present')
    
    if lungLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_lung_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_lung_lesion_status__exact= 'Present') 

    if liverLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_liver_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_liver_lesion_status__exact= 'Present')

    #Post-therapy
    if prostateLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Prostate')

    if nodeLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Lymph Nodes')
    
    if boneLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Bones')
    
    if lungLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Lungs')

    if liverLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Liver')
    
    #Follow-Up

    if prostateLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_prostate_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_prostate_lesion_status__exact= 'Present')

    if nodeLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_lymph_node_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_lymph_node_lesion_status__exact= 'Present')
    
    if boneLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_bone_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_bone_lesion_status__exact= 'Present')

    if brainLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_brain_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_brain_lesion_status__exact= 'Present')
    
    if lungLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_lung_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_lung_lesion_status__exact= 'Present') 

    if liverLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_liver_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_liver_lesion_status__exact= 'Present')

    count = patients.count

    context = {'patients': patients, 'patient_count' : count}
    return render(request, 'part_1/patient-list.html', context)

@login_required
def patientDetails(request, slug):
    patient = Patient.objects.get(slug=slug)
    physical_exam = PhysicalExam.objects.filter(patient=patient).first()
    screening = Screening.objects.filter(patient=patient).first()
    therapy = Therapy.objects.filter(patient=patient)
    post_therapy = PostTherapy.objects.filter(patient=patient)
    follow_up = FollowUp.objects.filter(patient=patient)

    context = {'patient' : patient, 'physical_exam' : physical_exam, 'screening' : screening, 'therapy' : therapy, 'post_therapy': post_therapy, 'follow_up' : follow_up}
    return render(request, 'part_1/patient-details.html', context)

@login_required
def patientSearch(request): 
    patients = Patient.objects.all()
    low_risk = request.GET.get('flexCheckLowRisk')
    intermediate_risk = request.GET.get('flexCheckIntermediateRisk')
    high_risk = request.GET.get('flexCheckHighRisk')
    bone_metastasis = request.GET.get('flexCheckMetastasis')
    side_effects = request.GET.get('flexCheckSideEffect')
    #Screening fields
    prostateLS = request.GET.get('flexCheckProstateL')
    nodeLS = request.GET.get('flexCheckLNL')
    boneLS = request.GET.get('flexCheckBoneL')
    brainLS = request.GET.get('flexCheckBrainL')
    lungLS = request.GET.get('flexCheckLungL')
    liverLS = request.GET.get('flexCheckLiverL')
    #Post-therapy fields
    prostateLPT = request.GET.get('flexCheckProstateLPT')
    nodeLPT = request.GET.get('flexCheckLNLPT')
    boneLPT = request.GET.get('flexCheckBoneLPT')
    lungLPT = request.GET.get('flexCheckLungLPT')
    liverLPT = request.GET.get('flexCheckLiverLPT')
    #Follow-up fields
    prostateLFU = request.GET.get('flexCheckProstateLFU')
    nodeLFU = request.GET.get('flexCheckLNLFU')
    boneLFU = request.GET.get('flexCheckBoneLFU')
    brainLFU = request.GET.get('flexCheckBrainLFU')
    lungLFU = request.GET.get('flexCheckLungLFU')
    liverLFU = request.GET.get('flexCheckLiverLFU')


    #Risk Assessment
    if low_risk == 'on':
        if intermediate_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')
        elif high_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk')
        else:
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk')

    if intermediate_risk == 'on':
        if low_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')
        elif high_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk')
        else:
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')

    if high_risk == 'on':
        if low_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Low Risk')
        elif intermediate_risk == 'on':
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'Intermediate Risk')
        else:
            patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__assessment__exact = 'High Risk')
    
    #Bone Metastasis
    if bone_metastasis == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__bone_metastasis_status = 'Metastasis')

    #Side Effect
    if side_effects == 'on':
        patients = Patient.objects.prefetch_related('t_patient').filter(t_patient__side_effects__isnull=False)

    #Screening Filters
    if prostateLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_prostate_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_prostate_lesion_status__exact= 'Present')

    if nodeLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_lymph_node_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_lymph_node_lesion_status__exact= 'Present')
    
    if boneLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_bone_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_bone_lesion_status__exact= 'Present')

    if brainLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_brain_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_brain_lesion_status__exact= 'Present')
    
    if lungLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_lung_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_lung_lesion_status__exact= 'Present') 

    if liverLS == 'on':
        patients = Patient.objects.prefetch_related('screening_patient').filter(screening_patient__gapsma_liver_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('screening_patient').filter(screening_patient__fdgpetct_liver_lesion_status__exact= 'Present')

    #Post-therapy
    if prostateLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Prostate')

    if nodeLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Lymph Nodes')
    
    if boneLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Bones')
    
    if lungLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Lungs')

    if liverLPT == 'on':
        patients = Patient.objects.prefetch_related('pt_patient').filter(pt_patient__lesions__exact= 'Liver')
    
    #Follow-Up

    if prostateLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_prostate_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_prostate_lesion_status__exact= 'Present')

    if nodeLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_lymph_node_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_lymph_node_lesion_status__exact= 'Present')
    
    if boneLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_bone_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_bone_lesion_status__exact= 'Present')

    if brainLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_brain_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_brain_lesion_status__exact= 'Present')
    
    if lungLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_lung_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_lung_lesion_status__exact= 'Present') 

    if liverLFU == 'on':
        patients = Patient.objects.prefetch_related('fu_patient').filter(fu_patient__gapsma_liver_lesion_status__exact= 'Present') | Patient.objects.prefetch_related('fu_patient').filter(fu_patient__fdgpetct_liver_lesion_status__exact= 'Present')

    
    count = patients.count
    if request.method == "POST":
        search = request.POST['search']
        results = Patient.objects.filter(name__contains=search)
        count = results.count
        context = {'search': search, 'results': results, 'patient_count' : count}
        return render(request, 'part_1/patient-search-results.html', context)
    else:
        context = {'results': patients, 'patient_count' : count}
        return render(request, 'part_1/patient-search-results.html', context)

@login_required
def addPatient(request):
    form = AddPatient()
    if request.method == "POST":
        form = AddPatient(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('patientList')
    context={'form':form}
    return render(request,"part_1/add-patient.html", context)

@login_required
def editPatient(request, slug):
    patient = Patient.objects.get(slug=slug)

    if request.method == "POST":
        form = EditPatient(request.POST, instance=patient)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect(reverse_lazy('patientList'))
    else:
        form = EditPatient(instance=patient)

        context = {'form' : form}
        return render(request, "part_1/edit-patient.html", context)

@login_required
def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('patientList')

@login_required
def addScreening(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddScreening()
    if request.method == "POST":
        form = AddScreening(request.POST, request.FILES)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_1/add-screening.html",context)

@login_required
def editScreening(request, slug, id):
    physical_exam = Screening.objects.get(id=id)
    if request.method == "POST":
        form = EditScreening(request.POST, instance=physical_exam)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditScreening(instance=physical_exam)
        context = {'form' : form}
        return render(request, "part_1/edit-screening.html", context)

@login_required
def deleteScreening(request, slug, id):
    screening = Screening.objects.get(id=id)
    screening.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def addPhysicalExam(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddPhysicalExam
    if request.method == "POST":
        form = AddPhysicalExam(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))

    context={'form':form, 'patient': patient}
    return render(request,"part_1/add-physical-exam.html",context)

@login_required
def editPhysicalExam(request, slug, id):
    physical_exam = PhysicalExam.objects.get(id=id)
    if request.method == "POST":
        form = EditPhysicalExam(request.POST, instance=physical_exam)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditPhysicalExam(instance=physical_exam)
        context = {'form' : form}
        return render(request, "part_1/edit-physical-exam.html", context)

@login_required 
def deletePhysicalExam(request, slug, id):
    physical_exam = PhysicalExam.objects.get(id=id)
    physical_exam.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def therapyList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = Therapy.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_2/therapy-list.html', context)

@login_required
def addTherapy(request, slug):
    patients = Patient.objects.all()
    patient = Patient.objects.get(slug=slug)
    form = AddTherapy()
    if request.method == "POST":
        form = AddTherapy(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_2/add-therapy.html",context)

@login_required
def editTherapy(request, slug, id):
    therapy = Therapy.objects.get(id=id)
    if request.method == "POST":
        form = EditTherapy(request.POST, instance=therapy)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditTherapy(instance=therapy)
        context = {'form' : form}
        return render(request, "part_2/edit-therapy.html", context)

@login_required
def deleteTherapy(request, slug, id):
    therapy = Therapy.objects.get(id=id)
    therapy.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def postTherapyList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = PostTherapy.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_3/post-therapy-list.html', context)

@login_required
def addPostTherapy(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddPostTherapy()
    if request.method == "POST":
        form = AddPostTherapy(request.POST, request.FILES)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
        
    context={'form':form, 'patient': patient}
    return render(request,"part_3/add-post-therapy.html",context)

@login_required
def editPostTherapy(request, slug, id):
    post_therapy = PostTherapy.objects.get(id=id)
    if request.method == "POST":
        form = EditPostTherapy(request.POST, instance=post_therapy)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditPostTherapy(instance=post_therapy)
        context = {'form' : form}
        return render(request, "part_3/edit-post-therapy.html", context)

@login_required
def deletePostTherapy(request, slug, id):
    post_therapy = PostTherapy.objects.get(id=id)
    post_therapy.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

@login_required
def followUpList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = FollowUp.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_4/follow-up-list.html', context)

@login_required
def addFollowUp(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddFollowUp()
    if request.method == "POST":
        form = AddFollowUp(request.POST, request.FILES)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('patientDetails',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_4/add-follow-up.html",context)

@login_required
def editFollowUp(request, slug, id):
    follow_up = FollowUp.objects.get(id=id)
    if request.method == "POST":
        form = EditFollowUp(request.POST, instance=follow_up)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))
    else:
        form = EditFollowUp(instance=follow_up)
        context = {'form' : form}
        return render(request, "part_4/edit-follow-up.html", context)

@login_required
def deleteFollowUp(request, slug, id):
    follow_up = FollowUp.objects.get(id=id)
    follow_up.delete()
    return HttpResponseRedirect(reverse_lazy('patientDetails', kwargs={"slug":slug}))

def viewPhysicalExam(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = PhysicalExam.objects.filter(patient=patient).first()

    context = {'list': list, 'patient': patient}
    return render(request, 'part_1/view-physical-exam.html', context)


def viewScreening(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = Screening.objects.filter(patient=patient).first()

    context = {'list': list, 'patient': patient}
    return render(request, 'part_1/view-screening.html', context)