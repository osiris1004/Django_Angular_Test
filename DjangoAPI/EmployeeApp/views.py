
from django.shortcuts import render

#The CSRF token ensures that forms originated from trusted domains can be used to POST 
# data back.
#csrf_exempt allow other domains to easily access our api methode
#from django.views.decorators import csrf_exempt
from django.views.decorators.csrf import csrf_exempt

#JSONParser use to pass the incomming data into data model
from rest_framework.parsers import JSONParser


from django.http.response import JsonResponse

#import both model
from EmployeeApp.models import Departments,Employees

#import the corresponding serializer
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

#import default_storage
from django.core.files.storage import default_storage



# Create your views here.
# the following below are our api method writen
@csrf_exempt

#The function departmentApi is performing Read Operation. In this function, we simply retrieve all 
# the objects in the Departments table. Those objects are then passed to the corresponding template.
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        # return all the data from department model in queryset format 

        departments_serializer = DepartmentSerializer(departments, many=True)
        #convert the JSON type to complex type (Model)

        return JsonResponse(departments_serializer.data, safe=False)
        #JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response. 
        # Its default Content-Type header is set to application/json. The first parameter, data, 
        # should be a dict instance. If the safe parameter is set to False, any object can be 
        # passed for serialization; otherwise only dict instances are allowed.

    elif request.method=='POST':
        #post methode use to insert values in department table
        department_data=JSONParser().parse(request)
        #JSONParser().parse convert the client send JSON object into Python native datatypes 
        department_serializer = DepartmentSerializer(data=department_data)
        #convert the JSON type to complex type (Model)
        if department_serializer.is_valid():
            # the is_valid() method to check whether the entered data is valid or not.
            # If the data is valid then is_valid() returns True, otherwise False.
            department_serializer.save()
            #save the model in to the data base
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        #put methode is use to update an exsiting method
        department_data = JSONParser().parse(request)
        #JSONParser().parse convert JSON object into Python native datatypes 
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        # get the exiting record  that should be updated 
        department_serializer=DepartmentSerializer(department,data=department_data)
        #map it with new values usinf the serializer class
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
        #get the value base on the pass id in your function
        department.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)



@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)



        

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    #extracting the uploaded file from the request

    file_name = default_storage.save(file.name,file)
    #default_storage.save(file.name,file) will anble us to save the file in the folder

    #return the file name
    return JsonResponse(file_name,safe=False)