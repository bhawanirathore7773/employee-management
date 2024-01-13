from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import Employee, Department, Role


# Create your views here.


def index(request):
    return render(request, 'index.html')


def emp_details(request):
    emps = Employee.objects.all()
    context={
        "emps":emps
    }
    return render(request, 'emp_details.html',context)


def add_emp(request):
    all_depart = Department.objects.all()
    all_role = Role.objects.all()
    context = {
        "all_depart":all_depart,
        "all_role":all_role
    }
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        number = request.POST["number"]
        department_id = request.POST.get("department")
        role_id = request.POST.get("role")
        department = Department.objects.get(id=department_id)
        print(department)
        role = Role.objects.get(id=role_id)
        salary = request.POST["salary"]
        location = request.POST["location"]
        add_employee = Employee(first_name=first_name, last_name=last_name,number=number, department=department, role=role, salary=salary, location=location)
        add_employee.save()
        return HttpResponse(f"User Details Submitted Successfully Department {department}")
    else:
        return render(request, 'add_emp.html',context)


def filter_emp(request):
    return render(request, 'filter_emp.html')


def remove(request,emp_id):
    context={
        "emp_id":emp_id
    }
    return render(request, 'remove.html', context)


def remove_emp(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    if request.method == 'POST':
        emp_id = request.POST.get("id")
        emp = get_object_or_404(Employee, id=int(emp_id))
        emp.delete()
        emps = Employee.objects.all()
        context={
            "emps":emps
        }
        return render(request, 'remove_emp.html', context)
    else:
        return render(request, 'remove_emp.html', context)
