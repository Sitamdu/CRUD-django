from django.db import models

# Create your models here.
class Detail(models.Model):
    firstname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.firstname
