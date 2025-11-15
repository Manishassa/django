from django.db import models

# Create your models here.
class register(models.Model):
    email=models.CharField(max_length=50)
    