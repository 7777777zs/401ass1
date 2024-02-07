from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer  # Create serializers.py for Employee model

class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all().order_by('years_with_company')
        serializer = EmployeeSerializer(employees, many=True)
        total_employees = len(employees)
        average_years = 0
        average_salary = 0
        if total_employees != 0:
            average_years = round(sum([employee.years_with_company for employee in employees]) / total_employees, 2)
            average_salary = round(sum([employee.salary for employee in employees]) / total_employees, 2)

        response_data = {
            "total": total_employees,
            "average_years_with_company": average_years,
            "average_salary": average_salary,
            "employees": serializer.data
        }

        return Response(response_data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "New employee added", "id": serializer.data["id"]}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee)
        RP = serializer.data
        RP.pop('id', None)
        return Response(RP)

    def put(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "Employee updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "Employee modified"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        return Response({"status": 200, "message": "Employee deleted"})
