from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homePage, name='homePage'),

    # path('patient/', views.patientList, name = 'patientList'),
    path('patient/add-patient/', views.addPatient, name='addPatient'),
    # path('patient/<slug:slug>', views.viewPatient, name='viewPatient'),

    # PHYSICAL EXAM
    # path('patient/<slug:slug>/physical-exam', views.physicalExam, name='physicalExam'), # Displays list of physical exam done
    # path('patient/<slug:slug>/physical-exam/add', views.addPhysicalExam, name='addPhysicalExam'),
    # path('patient/<slug:slug>/physical-exam/edit', views.editPhysicalExam, name='editPhysicalExam'),
    # CREATE condition to remove add physical exam since 1 : 1

    # SCREENING
    # path('patient/<slug:slug>/screening', views.screening, name='screening'), # Displays list of screening
    # path('patient/<slug:slug>/screening/add', views.addScreening, name='addScreening'),
    # path('patient/<slug:slug>/screening/edit/<slug:a>', views.editScreening, name='editScreening'),
    # path('patient/<slug:slug>/screening/view/<slug:a>', views.viewScreening, name= 'viewScreening'),
    # CREATE condition to remove add screening since 1 : 1

    # THERAPY
    # path('patient/<slug:slug>/therapy', views.therapy, name='therapy'),
    # path('patient/<slug:slug>/therapy/add', views.addTherapy, name='addTherapy'),
    # path('patient/<slug:slug>/therapy/edit/<slug:a>', views.editTherapy, name='editTherapy'),
    # path('patient/<slug:slug>/therapy/view/<slug:a>', views.viewTherapy, name='viewTherapy'),

    # POST-THERAPY
    # path('patient/<slug:slug>/post-therapy', views.postTherapy, name='postTherapy'),
    # path('patient/<slug:slug>/post-therapy/add', views.addPostTherapy, name='addPostTherapy'),
    # path('patient/<slug:slug>/post-therapy/edit/<slug:a>', views.editPostTherapy, name='editPostTherapy'),
    # path('patient/<slug:slug>/post-therapy/view/<slug:a>', views.viewPostTherapy, name='viewPostTherapy'),

    # FOLLOW-UP
    # path('patient/<slug:slug>/follow-up', views.followUp, name='followUp'),
    # path('patient/<slug:slug>/follow-up/add', views.addPostTherapy, name='addPostTherapy'),
    # path('patient/<slug:slug>/follow-up/edit/<slug:a>', views.editPostTherapy, name='editTherapy'),
    # path('patient/<slug:slug>/follow-up/view/<slug:a>', views.viewPostTherapy, name='viewPostTherapy'),

]