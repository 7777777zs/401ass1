from django.urls import path
from .views import EmployeeList, EmployeeDetail

urlpatterns = [
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('employees/<int:id>/', EmployeeDetail.as_view(), name='employee-detail'),
]
