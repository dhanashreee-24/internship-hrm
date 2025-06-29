
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_department, name='create_department'),
    path('dashboard/', views.department_list, name='department_list'),
    path('edit/<int:dept_id>/', views.edit_department, name='edit_department'),
    path('deactivate/<int:dept_id>/', views.deactivate_department, name='deactivate_department'),
    path('roles/', views.role_dashboard, name='role_dashboard'),
    path('roles/create/', views.create_role, name='create_role'),
    path('roles/edit/<int:role_id>/', views.edit_role, name='edit_role'),
    path('roles/delete/<int:role_id>/', views.delete_role, name='delete_role'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('departments/employees/', views.employee_dashboard, name='employee_dashboard'),
    path('departments/edit-employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('departments/delete-employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
]
