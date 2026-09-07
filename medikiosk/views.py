from django.shortcuts import render, redirect
from .forms import PatientForm


def patient_form(request):
    if request.method == "POST":
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("patient_success")

    else:
        form = PatientForm()

    return render(
        request,
        "medikiosk/patient/patient_form.html",
        {"form": form}
    )


def patient_success(request):
    return render(
        request,
        "medikiosk/patient/success.html"
    )
    
def patient_identify(request):
    return render (request,"medikiosk/patient/home.html")