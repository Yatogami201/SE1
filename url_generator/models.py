from django.db import models

class UniqueUrl (models.Model):
    url = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("unique_url_detail", kwargs={"unique_url": self.url})
