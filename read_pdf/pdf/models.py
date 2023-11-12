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
    

class File(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.name


class Chat(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question
