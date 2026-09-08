from django.shortcuts import render


def home(request):
    return render(
        request,
        "medikiosk/patient/home.html"
    )


def login_page(request):
    return render(
        request,
        "medikiosk/patient/LoginPage.html"
    )


def patient_form(request):
    return render(
        request,
        "medikiosk/patient/patient_form.html"
    )