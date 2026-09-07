from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "name",
            "age",
            "gender",
            "contact",
            "address",
            "abha",
            "complaint",
            "prakriti",
            "vikriti",
            "sara",
            "samhanana",
            "pramana",
            "satmya",
            "satva",
            "ahara_shakti",
            "vyayama_shakti",
            "vaya",
        ]
        
