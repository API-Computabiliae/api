from django.db import models

# Create your models here.


class Pdf(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default='') 

    def __str__(self):
        return self.name