Answer to questions 1,2,3 and 4 of assignment.

Run questions 1,3 and 4 normally from terminal fulfilling packages.

2 is a django app where an api is implemented. 
Create a django superuser or use the existing with us - admin pass - adminadmin
run the django app and open localhost:8000(check console log)

Then we can pass the following arguements with the address bar -

localhost:8000/insertEmployee/employeeId/firstName/lastName/
localhost:8000/insertDevice/deviceId/employeeId/
localhost:8000/updateEmployee/employeeId/firstName/lastName/
localhost:8000/updateDevice/deviceId/employeeId/
localhost:8000/deleteEmployee/employeeId/
localhost:8000/deleteDevice/deviceId/

To see the changes open admin using localhost:8000/admin and check Employee and Device model
