# import serializer from rest_framework module
from rest_framework import serializers

# import our complex types or models
from EmployeeApp.models import Departments, Employees

#The ModelSerializer class provides a shortcut that lets you automatically create a 
#Serializer class with fields that correspond to the Model fields.
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Department',
                  'DateOfJoining',
                  'PhotoFileName')
                  