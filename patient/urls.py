from django.urls import path
from . import views

urlpatterns = [
    path("Dashboard", views.dashboard, name="Dashboard"),
    path("Profile", views.profile, name="Profile"),
    path("BookAppointment", views.bookAppointment, name="BookAppointment"),
    path("AppointHistory", views.appointHistory, name="AppointHistory"),
]
