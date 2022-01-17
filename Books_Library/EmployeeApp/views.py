from django.shortcuts import render

#The CSRF token ensures that forms originated from trusted domains can be used to POST 
# data back.
#csrf_exempt allow other domains to easily access our api methode
from django.views.decorators import csrf_exempt

#JSONParser use to pass the incomming data into data model
from rest_framework.parser import JSONParser


from django.http.response import JsonResponse

#import both model
from EmployeeApp.models import Departments,Employees

#import the corresponding serializer
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer



# Create your views here.
# the following below are our api method writen
@csrf_exempt

#The function departmentApi is performing Read Operation. In this function, we simply retrieve all 
# the objects in the Departments table. Those objects are then passed to the corresponding template.
def departmentApi(request,id=0):
    if request.method=='GET':
        departments = Departments.objects.all()
        # return all the data from department model in json format(objects.all())

        departments_serializer = DepartmentSerializer(departments, many=True)
        # convert variable to json format
        return JsonResponse(departments_serializer.data, safe=False)
        #JsonResponse is an HttpResponse subclass that helps to create a JSON-encoded response. 
        # Its default Content-Type header is set to application/json. The first parameter
        # should be a dictionary instance. a second parameter name safe can be defind. if safe=fales,
        #it mean that The first parameter is  object passed for serialization; otherwise only dict instances are allowed

    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        department_data = JSONParser().parse(request)
        #JSONParser().parse convert JSON object in text format to 
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        department=Departments.objects.get(DepartmentId=id)
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
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)