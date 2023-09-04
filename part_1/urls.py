from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homePage, name='homePage'),

    path('register/', views.register, name='register'),
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
    path('patient/<slug:slug>/delete-pe/<int:id>/', views.deletePhysicalExam, name='deletePhysicalExam'),
    # CREATE condition to remove add physical exam since 1 : 1

    # SCREENING
    path('patient/<slug:slug>/screening', views.viewScreening, name='viewScreening'), # Displays list of screening
    path('patient/<slug:slug>/screening/add', views.addScreening, name='addScreening'),
    path('patient/<slug:slug>/screening/edit/<int:id>', views.editScreening, name='editScreening'),
    path('patient/<slug:slug>/delete-screening/<int:id>/', views.deleteScreening, name='deleteScreening'),
    # CREATE condition to remove add screening since 1 : 1

    # THERAPY
    path('patient/<slug:slug>/therapy', views.therapyList, name='therapyList'),
    path('patient/<slug:slug>/therapy/add', views.addTherapy, name='addTherapy'),
    path('patient/<slug:slug>/therapy/edit/<int:id>', views.editTherapy, name='editTherapy'),
    path('patient/<slug:slug>/delete-therapy/<int:id>/', views.deleteTherapy, name='deleteTherapy'),

    # POST-THERAPY
    path('patient/<slug:slug>/post-therapy', views.postTherapyList, name='postTherapyList'),
    path('patient/<slug:slug>/post-therapy/add', views.addPostTherapy, name='addPostTherapy'),
    path('patient/<slug:slug>/post-therapy/edit/<int:id>', views.editPostTherapy, name='editPostTherapy'),
    path('patient/<slug:slug>/delete-pt/<int:id>/', views.deletePostTherapy, name='deletePostTherapy'),

    # FOLLOW-UP
    path('patient/<slug:slug>/follow-up', views.followUpList, name='followUpList'),
    path('patient/<slug:slug>/follow-up/add', views.addFollowUp, name='addFollowUp'),
    path('patient/<slug:slug>/follow-up/edit/<int:id>', views.editFollowUp, name='editFollowUp'),
    path('patient/<slug:slug>/delete-fu/<int:id>/', views.deleteFollowUp, name='deleteFollowUp'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
