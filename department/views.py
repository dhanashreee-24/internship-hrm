from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Department, Role

def create_department(request):
    if request.method == 'POST':
        name = request.POST.get('dept_name')
        description = request.POST.get('description')

        if name:
            Department.objects.create(dept_name=name, description=description)
            messages.success(request, "Department created successfully!")
            return redirect('department_list')
        else:
            messages.error(request, "Department name is required.")

    return render(request, 'create.html')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'dashboard.html', {'departments': departments})

from django.shortcuts import get_object_or_404

def edit_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    
    if request.method == 'POST':
        department.dept_name = request.POST.get('dept_name')
        department.description = request.POST.get('description')
        department.save()
        messages.success(request, "Department updated successfully!")
        return redirect('department_list')

    return render(request, 'edit.html', {'department': department})

from django.http import HttpResponseRedirect


def deactivate_department(request, dept_id):
    department = get_object_or_404(Department, id=dept_id)
    department.status = False
    department.save()

    messages.success(request, "Department deactivated successfully.")
    return redirect('department_list')


def create_role(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if name:
            Role.objects.create(name=name, description=description)
            messages.success(request, "Role created successfully!")
            return redirect('role_dashboard')
        else:
            messages.error(request, "Role name is required.")

    return render(request, 'create_role.html')

def role_dashboard(request):
    roles = Role.objects.all()
    return render(request, 'role_dashboard.html', {'roles': roles})

from django.shortcuts import get_object_or_404

def edit_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)

    if request.method == 'POST':
        role.name = request.POST.get('name')
        role.description = request.POST.get('description')
        role.save()
        messages.success(request, "Role updated successfully!")
        return redirect('role_dashboard')

    return render(request, 'edit_role.html', {'role': role})

def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    role.status = False  # Soft delete
    role.save()
    messages.success(request, "Role deactivated successfully.")
    return redirect('role_dashboard')

from django.shortcuts import render, redirect
from .models import CustomUser, Department, Role
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CustomUser, Department, Role
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Department, Role

def add_employee(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        username = request.POST.get('username')
        password = request.POST.get('password')
        department_id = request.POST.get('department')
        role_id = request.POST.get('role')
        reporting_id = request.POST.get('reporting_manager')
        date_of_joining = request.POST.get('date_of_joining')

        # Check required fields
        if not all([first_name, last_name, email, username, password, department_id, role_id, date_of_joining]):
            messages.error(request, "All required fields must be filled.")
            return redirect('add_employee')

        department = get_object_or_404(Department, id=department_id)
        role = get_object_or_404(Role, id=role_id)
        reporting_manager = CustomUser.objects.filter(id=reporting_id).first() if reporting_id else None

        CustomUser.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            username=username,
            password=make_password(password),
            department=department,
            role=role,
            reporting_manager=reporting_manager,
            date_of_joining=date_of_joining,
            status=True
        )

        messages.success(request, "Employee added successfully.")
        return redirect('employee_dashboard')

    context = {
        'departments': Department.objects.filter(status=True),
        'roles': Role.objects.filter(status=True),
        'managers': CustomUser.objects.all()
    }
    return render(request, 'add_employee.html', context)


def employee_dashboard(request):
    employees = CustomUser.objects.select_related('department', 'role', 'reporting_manager').all()
    return render(request, 'employee_dashboard.html', {'employees': employees})

# Edit employee
def edit_employee(request, employee_id):
    employee = get_object_or_404(CustomUser, id=employee_id)

    if request.method == 'POST':
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.email = request.POST['email']
        employee.mobile = request.POST['mobile']
        employee.username = request.POST['username']
        new_password = request.POST.get('password')
        if new_password:
            employee.password = make_password(new_password)
        employee.department_id = request.POST['department']
        employee.role_id = request.POST['role']
        employee.reporting_manager_id = request.POST.get('reporting_manager') or None
        employee.date_of_joining = request.POST['date_of_joining']
        employee.save()
        messages.success(request, 'Employee updated successfully.')
        return redirect('employee_dashboard')

    context = {
        'employee': employee,
        'departments': Department.objects.all(),
        'roles': Role.objects.all(),
        'managers': CustomUser.objects.exclude(id=employee.id)
    }
    return render(request, 'edit_employee.html', context)

# Delete employee
def delete_employee(request, employee_id):
    employee = get_object_or_404(CustomUser, id=employee_id)
    employee.delete()
    messages.success(request, 'Employee deleted successfully.')
    return redirect('employee_dashboard')

