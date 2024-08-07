# doctor_portal/models.py

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()  # Years of experience
    qualification = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    # Other fields specific to doctors

    def __str__(self):
        return self.name

