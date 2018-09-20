from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Employee,Device

def insert_employee(request,employeeId,firstName,lastName):
    if(employeeId!='None' and firstName!='None' and lastName!='None'):
        new_employee_instance = Employee(EmployeeId=employeeId,First_Name=firstName,Last_Name=lastName)
        new_employee_instance.save()
        return HttpResponse('<h1>Success</h1>')

def insert_device(request,deviceId,employeeId):
    if(deviceId!='None'):
        employeeInstance = get_object_or_404(Employee,EmployeeId=employeeId)
        new_device_instance = Device(DeviceId=deviceId,employee=employeeInstance)
        new_device_instance.save()
        return HttpResponse('<h1>Success</h1>')

def update_employee(request,employeeId,firstName,lastName):
        instance = get_object_or_404(Employee,EmployeeId=employeeId)
        fields = []
        if(firstName!='None'):
            fields.append('First_Name')
            instance.First_Name = firstName
        if(lastName!='None'):
            fields.append('Last_Name')
            instance.Last_Name = lastName
        instance.save(update_fields=fields)
        return HttpResponse('<h1>Success</h1>')
        

def update_device(request,deviceId,employeeId):
    deviceInstance = get_object_or_404(Device,DeviceId=deviceId)
    employeeInstance = get_object_or_404(Employee,EmployeeId=employeeId)
    deviceInstance.employee = employeeInstance
    deviceInstance.save()
    return HttpResponse('<h1>Success</h1>')

def delete_employee(request,employeeId):
        instance = get_object_or_404(Employee,EmployeeId=employeeId)
        instance.delete()
        return HttpResponse('<h1>Success</h1>')
        

def delete_device(request,deviceId):
    deviceInstance = get_object_or_404(Device,DeviceId=deviceId)
    deviceInstance.delete()
    return HttpResponse('<h1>Success</h1>')