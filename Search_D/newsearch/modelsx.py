from django.db import models
from django.utils import timezone


class TestModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    #author = models.ForeignKey(settings.AUTH_USER_MODEL)
    publication_date = models.DateTimeField(default=timezone.now)
