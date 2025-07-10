from django.db import models

class Employee (models.Model):
    employee_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    department=models.CharField(max_length=100)

