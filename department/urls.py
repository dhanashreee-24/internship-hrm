
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_department, name='create_department'),
    path('dashboard/', views.department_list, name='department_list'),
    path('edit/<int:dept_id>/', views.edit_department, name='edit_department'),
    path('deactivate/<int:dept_id>/', views.deactivate_department, name='deactivate_department'),
]
