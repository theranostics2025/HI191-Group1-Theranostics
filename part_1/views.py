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

from django.db.models import Exists, OuterRef, Q

from django.core.paginator import Paginator

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

    # Assessment Type (Only one of them is possible)
    risk_types = {
        'flexCheckLowRisk': 'Low Risk',
        'flexCheckIntermediateRisk': 'Intermediate Risk',
        'flexCheckHighRisk': 'High Risk'
    }
    selected_risk = next(
        (label for key, label in risk_types.items() if request.GET.get(key) == 'on'), None
    )
    if selected_risk:
        patients = patients.filter(
            screening_patient__assessment__exact=selected_risk
        )

    # Metastasis
    if request.GET.get('flexHasMetastasis') == 'on':
        patients = patients.filter(
            screening_patient__bone_metastasis_status='With Metastasis'
        )

    # Side Effects
    if request.GET.get('flexHasSideEffect') == 'on':
        patients = patients.filter(
            Exists(
                Therapy.objects.filter(
                    patient_id=OuterRef('pk')
                ).filter(
                    ~Q(side_effects__isnull=True) & ~Q(side_effects__exact='')
                )
            )
        )

    # Screening Imaging
    screening_filters = {
        'flexCheckProstateL': Q(screening_patient__gapsma_prostate_lesion_status='Present') | Q(screening_patient__fdgpetct_prostate_lesion_status='Present'),
        'flexCheckLNL': Q(screening_patient__gapsma_lymph_node_lesion_status='Present') | Q(screening_patient__fdgpetct_lymph_node_lesion_status='Present'),
        'flexCheckBoneL': Q(screening_patient__gapsma_bone_lesion_status='Present') | Q(screening_patient__fdgpetct_bone_lesion_status='Present'),
        'flexCheckBrainL': Q(screening_patient__gapsma_brain_lesion_status='Present') | Q(screening_patient__fdgpetct_brain_lesion_status='Present'),
        'flexCheckLungL': Q(screening_patient__gapsma_lung_lesion_status='Present') | Q(screening_patient__fdgpetct_lung_lesion_status='Present'),
        'flexCheckLiverL': Q(screening_patient__gapsma_liver_lesion_status='Present') | Q(screening_patient__fdgpetct_liver_lesion_status='Present'),
    }

    for key, condition in screening_filters.items():
        if request.GET.get(key) == 'on':
            patients = patients.filter(condition)

    # Post-Therapy Imaging
    post_therapy_filters = {
        'flexCheckProstateLPT': Q(pt_patient__lesions__icontains='Prostate'),
        'flexCheckLNLPT': Q(pt_patient__lesions__icontains='Lymph Nodes'),
        'flexCheckBoneLPT': Q(pt_patient__lesions__icontains='Bones'),
        'flexCheckLungLPT': Q(pt_patient__lesions__icontains='Lungs'),
        'flexCheckLiverLPT': Q(pt_patient__lesions__icontains='Liver'),
    }

    for key, condition in post_therapy_filters.items():
        if request.GET.get(key) == 'on':
            patients = patients.filter(condition)

    # Follow-up Imaging
    followup_filters = {
        'flexCheckProstateLFU': Q(fu_patient__gapsma_prostate_lesion_status='Present') | Q(fu_patient__fdgpetct_prostate_lesion_status='Present'),
        'flexCheckLNLFU': Q(fu_patient__gapsma_lymph_node_lesion_status='Present') | Q(fu_patient__fdgpetct_lymph_node_lesion_status='Present'),
        'flexCheckBoneLFU': Q(fu_patient__gapsma_bone_lesion_status='Present') | Q(fu_patient__fdgpetct_bone_lesion_status='Present'),
        'flexCheckBrainLFU': Q(fu_patient__gapsma_brain_lesion_status='Present') | Q(fu_patient__fdgpetct_brain_lesion_status='Present'),
        'flexCheckLungLFU': Q(fu_patient__gapsma_lung_lesion_status='Present') | Q(fu_patient__fdgpetct_lung_lesion_status='Present'),
        'flexCheckLiverLFU': Q(fu_patient__gapsma_liver_lesion_status='Present') | Q(fu_patient__fdgpetct_liver_lesion_status='Present'),
    }

    for key, condition in followup_filters.items():
        if request.GET.get(key) == 'on':
            patients = patients.filter(condition)

    # Finalize
    patients = patients.distinct().order_by('id')
    count = patients.count()

    context = {'patients': patients, 'patient_count': count}
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
    if request.method == "POST":
        form = AddPatient(request.POST, request.FILES)
        if form.is_valid():
            try:
                patient = form.save()
                return redirect('patientList')
            except Exception as e:
                messages.error(request, f"Error saving patient: {str(e)}")
    else:
        form = AddPatient()

    context = {'form': form}
    return render(request, "part_1/add-patient.html", context)


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