from django.urls import path
from . import views

urlpatterns = [
    path("", views.patient_identify, name="home"),
    path("patient/", views.patient_form, name="patient_form"),
    path(
        "patient/success/",
        views.patient_success,
        name="patient_success"
    ),
]