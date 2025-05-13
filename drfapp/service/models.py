from django.db import models

class ServiceAppointment(models.Model):
    customer_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.car_model}"
