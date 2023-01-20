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

def homePage(request):
    return render(request, 'part_1/home-page.html')

def patientList(request):
    patients = Patient.objects.all()

    context = {'patients': patients}
    return render(request, 'part_1/patient-list.html', context)

def addPatient(request):
    form = AddPatient()
    if request.method == "POST":
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context={'form':form}
    return render(request,"part_1/add-patient.html", context)

def addScreening(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddScreening()
    if request.method == "POST":
        form = AddScreening(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('viewScreening',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_1/add-screening.html",context)

def addPhysicalExam(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddPhysicalExam
    if request.method == "POST":
        form = AddPhysicalExam(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('viewPhysicalExam',kwargs={'slug':slug}))

    context={'form':form, 'patient': patient}
    return render(request,"part_1/add-physical-exam.html",context)

def therapyList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = Therapy.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_2/therapy-list.html', context)

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
            return redirect(reverse('therapyList',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_2/add-therapy.html",context)

def postTherapyList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = PostTherapy.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_3/post-therapy-list.html', context)

def addPostTherapy(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddPostTherapy()
    if request.method == "POST":
        form = AddPostTherapy(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('postTherapyList',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_3/add-post-therapy.html",context)

def followUpList(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = FollowUp.objects.filter(patient=patient).order_by('-pk')

    context = {'list': list, 'patient': patient}
    return render(request, 'part_4/follow-up-list.html', context)

def addFollowUp(request, slug):
    patient = Patient.objects.get(slug=slug)
    form = AddFollowUp()
    if request.method == "POST":
        form = AddFollowUp(request.POST)
        if form.is_valid():
            build = form.save(False)
            build.patient = patient
            build.save()
            return redirect(reverse('followUpList',kwargs={'slug':slug}))
# def
    context={'form':form, 'patient': patient}
    return render(request,"part_4/add-follow-up.html",context)

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

def viewScreening(request, slug):
    patient = Patient.objects.get(slug=slug)
    list = Screening.objects.filter(patient=patient).first()

    context = {'list': list, 'patient': patient}
    return render(request, 'part_1/view-screening.html', context)