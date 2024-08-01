# admin_panel/urls.py

from django.urls import path
from .views import AppointmentListCreateAPIView, AppointmentRetrieveUpdateDestroyAPIView
from .views import protected_view, signup

urlpatterns = [
    path('appointments/', AppointmentListCreateAPIView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyAPIView.as_view(), name='appointment-retrieve-update-destroy'),
    path('protected/',protected_view, name='admin_protected_view'),
    path('signup/', signup, name='signup'),
]
