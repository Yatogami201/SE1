from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'rates'

    def __str__(self):
        return self.name
    
    