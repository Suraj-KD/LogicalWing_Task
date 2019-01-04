from django.db import models


# Create your models here.
class Medicine_Type(models.Model):
    medicine_type = models.CharField(max_length=40)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def  __str__(self):
        return self.medicine_type


class Medicine_Detail(models.Model):
    medicine_type = models.ForeignKey(Medicine_Type, on_delete=models.CASCADE, )
    name = models.CharField(max_length=40)
    descriptions = models.TextField(max_length=100)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    expired = models.DateTimeField()

    def __str__(self):
        return self.name
