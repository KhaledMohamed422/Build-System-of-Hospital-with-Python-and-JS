from django.urls import path
from . import views

urlpatterns = [
    path("Dashboard", views.Dashboard, name="manger_Dashboard"),
    path("AddDoctor", views.AddDoctor, name="AddDoctor"),
    path("Appointment", views.myAppointment, name="myAppointment"),
    path("ManagePatient", views.ManagePatient, name="ManagePatient"),
    path("ManageUser", views.ManageUser, name="ManageUser"),
    path("ManageDoctor", views.ManageDoctor, name="ManageDoctor"),
    path("EditSpecification", views.EditSpecification, name="EditSpecification"),
    path("PatientData", views.PatientData, name="PatientData"),
]
