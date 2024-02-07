# employees/models.py

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    years_with_company = models.FloatField()
    salary = models.FloatField()
    def __str__(self):
        return self.name