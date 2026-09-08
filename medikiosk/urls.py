from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("login/", views.login_page, name="login"),
    path("patient_form/", views.patient_form, name="patient_form"),
]