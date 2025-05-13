from rest_framework import viewsets
from .models import ServiceAppointment
from .serializers import ServiceAppointmentSerializer

class ServiceAppointmentViewSet(viewsets.ModelViewSet):
    queryset = ServiceAppointment.objects.all()
    serializer_class = ServiceAppointmentSerializer
