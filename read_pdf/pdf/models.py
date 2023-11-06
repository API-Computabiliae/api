from django.db import models

# Create your models here.


class Pdf(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default='')

    def __str__(self):
        return self.name
    

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name