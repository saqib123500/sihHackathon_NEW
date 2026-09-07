from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "age",
        "gender",
        "contact",
        "complaint",
        "created_at",
    )

    search_fields = (
        "name",
        "contact",
        "abha",
    )