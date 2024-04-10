from django.db import models

class UniqueUrl (models.Model):
    url = models.CharField(max_length=100, unique=True)

