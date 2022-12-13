from django.urls import path
from . import views


urlpatterns = [
    path("Dashboard", views.dashboard, name="dr_Dashboard"),
    path("Profile", views.profile, name="dr_Profile"),
    path("myAppointment", views.myAppointment, name="myAppointment"),
    path("patients", views.patientslist, name="patientslist"),
]
