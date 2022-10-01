from django.db import models

# Create your models here.
class corona19_model(models.Model):
    totalcases = models.CharField(max_length=200)
    totaldeaths = models.CharField(max_length=200)
    totalrecovered = models.CharField(max_length=200)
    