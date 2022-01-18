
# import serializer from rest_framework module
from rest_framework import serializers

# import our complex types or models
from EmployeeApp.models import Departments, Employees

#Serializers allow complex data such as querysets and model instances to be converted to 
# native Python datatypes that can then be easily rendered into JSON, XML or other content 
# types. Serializers also provide deserialization, allowing parsed data to be converted back 
# into complex types, after first validating the incoming data.

#Serializer   = : Python native datatypes(dictionary,querysets and model instances) -> JSON
#Deserializer = : JSON -> Python native datatypes(dictionary,querysets and model instances) // need to be validated
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
                  
                  