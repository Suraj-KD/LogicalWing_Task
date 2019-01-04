from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    DOJ = models.DateField(default=timezone.now)
    address = models.TextField(max_length=100)
    city = models.CharField(max_length=20)
    DOB = models.DateField()
    salary = models.IntegerField(default=0)

    class Meta:
        ordering = ('DOJ',)