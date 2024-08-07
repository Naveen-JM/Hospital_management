# patient_portal/models.py

from django.db import models


class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=15)

    # Other fields specific to patients

    def __str__(self):
        return self.name

# patient_portal/models.py

from django.db import models

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    current_symptoms = models.TextField()
    physical_examination = models.TextField()
    treatment_plan = models.TextField()
    prescription = models.TextField()  # Include medicine name with 0-0-1 AF(after food)/BF(before food)

    def __str__(self):
        return f"Medical Record for {self.patient.name}"
