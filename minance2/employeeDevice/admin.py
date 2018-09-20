from django.contrib import admin

# Register your models here.

from employeeDevice.models import Employee,Device

class EmployeeModelAdmin(admin.ModelAdmin):
	list_display = ["EmployeeId","First_Name","Last_Name"]
	list_filter = ["EmployeeId"]
	search_fields = ["EmployeeId","First_Name"]
	class Meta:
		model = Employee

class DeviceModelAdmin(admin.ModelAdmin):
	list_display = ["DeviceId","employee"]
	list_filter = ["DeviceId"]
	search_fields = ["DeviceId"]
	class Meta:
		model = Device

admin.site.register(Employee,EmployeeModelAdmin)
admin.site.register(Device,DeviceModelAdmin)
