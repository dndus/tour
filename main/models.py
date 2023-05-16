from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.FileField(upload_to='media')