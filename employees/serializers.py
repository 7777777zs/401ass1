# employees/serializers.py

from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Convert years_with_company to integer if it's a whole number
        data['years_with_company'] = int(data['years_with_company']) if data['years_with_company'].is_integer() else \
        data['years_with_company']
        # Convert salary to integer if it's a whole number
        data['salary'] = int(data['salary']) if data['salary'].is_integer() else data['salary']
        return data