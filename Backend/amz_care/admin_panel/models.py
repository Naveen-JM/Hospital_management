# admin_panel/models.py

from django.db import models
from patient_portal.models import Patient  # Import Patient model from patient_portal app
from doctor_portal.models import Doctor # Import Doctor model from doctor_portal app


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ]

    date_time = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    # Other fields
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=Patient.GENDER_CHOICES)
    contact_information = models.CharField(max_length=15)
    symptoms = models.TextField()
    nature_of_visit = models.CharField(max_length=100)
    preferred_date_time = models.DateTimeField()

    def __str__(self):
        return f"Appointment with {self.doctor.name} on {self.date_time}"
