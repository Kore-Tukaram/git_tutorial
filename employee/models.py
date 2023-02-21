from django.db import models

# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=50)
    uid = models.IntegerField()
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name
