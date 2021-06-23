from employee_register.forms import EmployeeForm
from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request,"employee_registers/employee_list.html",context)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:                          # if it is insert populate empty form
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)      #delete operation populate this form
            form = EmployeeForm(instance=employee)
        return render(request,"employee_registers/employee_form.html",{'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')           #page will redirect to the list page

def employee_delete(request):
    return 

