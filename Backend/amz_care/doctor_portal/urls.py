# doctor_portal/urls.py

from django.urls import path
from .views import DoctorListCreateAPIView, DoctorRetrieveUpdateDestroyAPIView
from .views import DoctorProtectedView

urlpatterns = [
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyAPIView.as_view(), name='doctor-retrieve-update-destroy'),
    path('protected/', DoctorProtectedView.as_view(), name='doctor_protected_view'),
]
