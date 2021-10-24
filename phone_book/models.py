from django.db import models

# Create your models here.
class phonebook(models.Model):
    name = models.CharField(max_length=100)
    phonenum = models.IntegerField()
    address = models.CharField(max_length=150)
    email = models.EmailField(max_length = 100)
