from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeId = models.CharField(max_length=30,unique=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)

class Device(models.Model):
    DeviceId = models.CharField(max_length=30,unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)