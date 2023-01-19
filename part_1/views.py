from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . forms import *
from . models import *

def homePage(request):
    return render(request, 'part_1/home-page.html')

def addPatient(request):
    form = AddPatient()
    if request.method == "POST":
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context={'form':form}
    return render(request,"part_1/add-patient.html", context)