# ✅Assignment(CRUD Operations)
## 📅Date: 10/07/2025
### Task
  Develop an **Employee Directory App** using Django. Admins should be able to manage employee profiles using CRUD operations. Fields include employee name, job title, email, and department. Use Django templates to show the employee list and provide modals or forms for creating and updating employee data.
### Program
models.py

```
from django.db import models

class Employee (models.Model):
    employee_name=models.CharField(max_length=100)
    job_title=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    department=models.CharField(max_length=100)

```
views.py

```
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.shortcuts import get_object_or_404,redirect

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method =='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form=EmployeeForm()
    
    return render(request,'employee_form.html',{'form':form})

def employee_update(request,pk):
    employee = Employee.objects.get(pk=pk)
    if request.method =='POST':
        form = EmployeeForm(request.POST, instance=employee)
        form.save()
        return redirect('employee_list')
    else:
        form=EmployeeForm(instance=employee)
    return render(request,'employee_form.html',{'form':form})
def employee_delete(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    if request.method=='POST':
        employee.delete()
        return redirect('employee_list')
    return render(request,'employee_confirm_delete.html',{'employee':employee})
```
## Output

**Create**

<img width="1918" height="1087" alt="image" src="https://github.com/user-attachments/assets/f94a8820-faa2-40c6-945b-aa2789d0b5c0" />

**Read**

<img width="1910" height="1087" alt="image" src="https://github.com/user-attachments/assets/dd4a28a6-e92d-488d-a65c-168d130e1476" />

**Update**

<img width="1918" height="1090" alt="image" src="https://github.com/user-attachments/assets/1a94ea2a-73f4-44ca-af55-1f389256a831" />

**Delete**

<img width="1917" height="1091" alt="image" src="https://github.com/user-attachments/assets/6c12de74-777f-418c-893f-b4fec446116e" />


