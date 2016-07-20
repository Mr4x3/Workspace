from django.db import models

# Create your models here.

class Post(model.Model):
    title=model.CharField(max_length=140)
