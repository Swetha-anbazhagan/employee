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