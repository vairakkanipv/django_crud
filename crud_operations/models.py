from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=150)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name;

