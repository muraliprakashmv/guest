from django.db import models
from django.utils import timezone

# Create your models here.



class student(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,unique=True)
    address=models.CharField(max_length=250)
    gender=models.CharField(max_length=10)
    joining_date = models.CharField(max_length=50,default=timezone.now())
    updated = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table='student'
