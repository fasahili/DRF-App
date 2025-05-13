from rest_framework import serializers
from .models import ServiceAppointment

class ServiceAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAppointment
        fields = '__all__'
