# patient_portal/urls.py

from django.urls import path
from .views import (MedicalRecordListCreateAPIView, MedicalRecordRetrieveUpdateDestroyAPIView,
                    PatientListCreateAPIView, PatientRetrieveUpdateDestroyAPIView, MedicalRecordListByPatientAPIView)
from .views import PatientProtectedView

urlpatterns = [
    path('medical-records/', MedicalRecordListCreateAPIView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordRetrieveUpdateDestroyAPIView.as_view(), name='medical-record-retrieve-update-destroy'),
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyAPIView.as_view(), name='patient-retrieve-update-destroy'),
    path('medical-records/patient/<int:patient_id>/', MedicalRecordListByPatientAPIView.as_view(), name='medical-record-list-by-patient'),
path('protected/', PatientProtectedView.as_view(), name='patient_protected_view'),
]
