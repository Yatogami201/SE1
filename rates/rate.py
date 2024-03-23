from django.db import models
from .service import Service
from django.contrib.auth.models import User

class Rate(models.Model):
    RATE_TYPE_CHOICES = [
        ('hourly', 'Hourly'),
        ('per_project', 'Per Project'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rate_type = models.CharField(max_length=20, choices=RATE_TYPE_CHOICES)
    rate_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.service.name} - {self.rate_type} - {self.rate_amount}"

