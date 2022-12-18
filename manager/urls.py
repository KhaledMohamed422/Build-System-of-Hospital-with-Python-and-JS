from django.urls import path
from . import views

urlpatterns = [
    path("Dashboard", views.Dashboard, name="Dashboard"),
    path("AddDoctor", views.AddDoctor, name="AddDoctor"),
    path("Appointment", views.myAppointment, name="myAppointment"),
    path("AddSpecification", views.AddSpecification, name="AddSpecification"),
    path("AddUser", views.AddUser, name="AddUser"),
    

    path("ManagePatient", views.ManagePatient, name="ManagePatient"),
    path("ManageUser", views.ManageUser, name="ManageUser"),
    path("ManageDoctor", views.ManageDoctor, name="ManageDoctor"),
    path("ManageSpecification", views.ManageSpecification, name="ManageSpecification"),
    
    # path('delete/<int:id>', views.deletbook, name='delete'),
    path('descrption/<int:id>', views.descrption, name='descrption'),

]
