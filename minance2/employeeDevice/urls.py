from django.urls import path
from . import views

urlpatterns = [
        path('insertEmployee/<str:employeeId>/<str:firstName>/<str:lastName>/',views.insert_employee,name='insert_employee'),
        path('insertDevice/<str:deviceId>/<str:employeeId>/',views.insert_device,name='insert_device'),
        path('updateEmployee/<str:employeeId>/<str:firstName>/<str:lastName>/',views.update_employee,name='update_employee'),
        path('updateDevice/<str:deviceId>/<str:employeeId>/',views.update_device,name='update_device'),
	path('deleteEmployee/<str:employeeId>/',views.delete_employee,name='delete_employee'),
        path('deleteDevice/<str:deviceId>/',views.delete_device,name='delete_device')
]