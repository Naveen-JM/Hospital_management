# patient_portal/views.py

from rest_framework import generics
from .models import Patient,MedicalRecord
from .serializers import PatientSerializer,MedicalRecordSerializer

class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalRecordListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class MedicalRecordRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer

class MedicalRecordListByPatientAPIView(generics.ListAPIView):
    serializer_class = MedicalRecordSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return MedicalRecord.objects.filter(patient_id=patient_id)

# views.py in one of your apps

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PatientProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Your protected view logic here
        user = request.user
        return Response({"message": f"Hello, {user.username}! You're authenticated."})
