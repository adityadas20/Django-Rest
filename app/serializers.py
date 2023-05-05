from .models import Employee
from django.contrib.auth.models import User
from rest_framework import serializers


# class EmployeeSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     email = serializers.EmailField(default="temp@temp.com")
#     password = serializers.CharField(max_length=50)
#     phone = serializers.CharField(max_length=10)

#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self, employee, validated_data):
#         newEmployee = Employee(**validated_data)
#         newEmployee.id = employee.id
#         newEmployee.save()
#         return newEmployee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields=['name', 'email']
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     # email = serializers.EmailField(default="temp@temp.com")
