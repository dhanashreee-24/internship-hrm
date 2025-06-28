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


