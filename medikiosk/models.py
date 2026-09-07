from django.db import models

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]

    VAYA_CHOICES = [
        ("childhood", "Childhood"),
        ("middle_age", "Middle Age"),
        ("old_age", "Old Age"),
    ]

    # Basic Details
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    abha = models.CharField(max_length=50, blank=True)
    complaint = models.TextField()

    # Dashavidha Pariksha
    prakriti = models.TextField()
    vikriti = models.TextField()
    sara = models.TextField()
    samhanana = models.TextField()
    pramana = models.TextField()
    satmya = models.TextField()
    satva = models.TextField()
    ahara_shakti = models.TextField()
    vyayama_shakti = models.TextField()
    vaya = models.CharField(max_length=20, choices=VAYA_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name