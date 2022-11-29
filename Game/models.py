from django.db import models

# Create your models here.
class GRA(models.Model):
    gracz = models.CharField(max_length=50, blank=True, null=True)
    wynik = models.IntegerField(blank=True, null=True)

