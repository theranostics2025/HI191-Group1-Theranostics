from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homePage, name='homePage'),

    path('patient/', views.patientList, name = 'patientList'),
    path('patient-search/', views.patientSearch, name = 'patientSearch'),
    path('patient/add-patient/', views.addPatient, name='addPatient'),
    path('patient/edit-patient/<slug:slug>', views.editPatient, name='editPatient'),
    path('patient/<slug:slug>', views.patientDetails, name='patientDetails'),
    path('patient/delete/<int:pk>/', views.deletePatient, name='deletePatient'),

    # PHYSICAL EXAM
    path('patient/<slug:slug>/view-physical-exam', views.viewPhysicalExam, name='viewPhysicalExam'), # Displays list of physical exam done
    path('patient/<slug:slug>/physical-exam/add', views.addPhysicalExam, name='addPhysicalExam'),
    path('patient/<slug:slug>/physical-exam/edit/<int:id>', views.editPhysicalExam, name='editPhysicalExam'),
    # CREATE condition to remove add physical exam since 1 : 1

    # SCREENING
    path('patient/<slug:slug>/screening', views.viewScreening, name='viewScreening'), # Displays list of screening
    path('patient/<slug:slug>/screening/add', views.addScreening, name='addScreening'),
    # path('patient/<slug:slug>/screening/edit/<slug:a>', views.editScreening, name='editScreening'),
    # path('patient/<slug:slug>/screening/view/<slug:a>', views.viewScreening, name= 'viewScreening'),
    # CREATE condition to remove add screening since 1 : 1

    # THERAPY
    path('patient/<slug:slug>/therapy', views.therapyList, name='therapyList'),
    path('patient/<slug:slug>/therapy/add', views.addTherapy, name='addTherapy'),
    path('patient/<slug:slug>/therapy/edit/<int:id>', views.editTherapy, name='editTherapy'),
    # path('patient/<slug:slug>/therapy/view/<slug:a>', views.viewTherapy, name='viewTherapy'),

    # POST-THERAPY
    path('patient/<slug:slug>/post-therapy', views.postTherapyList, name='postTherapyList'),
    path('patient/<slug:slug>/post-therapy/add', views.addPostTherapy, name='addPostTherapy'),
    path('patient/<slug:slug>/post-therapy/edit/<int:id>', views.editPostTherapy, name='editPostTherapy'),
    # path('patient/<slug:slug>/post-therapy/view/<slug:a>', views.viewPostTherapy, name='viewPostTherapy'),

    # FOLLOW-UP
    path('patient/<slug:slug>/follow-up', views.followUpList, name='followUpList'),
    path('patient/<slug:slug>/follow-up/add', views.addFollowUp, name='addFollowUp'),
    # path('patient/<slug:slug>/follow-up/edit/<slug:a>', views.editPostTherapy, name='editTherapy'),
    # path('patient/<slug:slug>/follow-up/view/<slug:a>', views.viewPostTherapy, name='viewPostTherapy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
