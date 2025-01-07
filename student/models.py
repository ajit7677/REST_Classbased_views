from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    country = models.CharField(max_length=15)
    email = models.EmailField()