from django.contrib import admin
from .models import Department, Role, CustomUser
from django.contrib.auth.admin import UserAdmin


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Department._meta.fields]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Role._meta.fields]


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('mobile', 'department', 'role', 'reporting_manager', 'date_of_joining', 'status')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('mobile', 'department', 'role', 'reporting_manager', 'date_of_joining', 'status')
        }),
    )
    list_display = ['username', 'first_name', 'last_name', 'email', 'department', 'role', 'reporting_manager', 'status']


admin.site.site_header = "HRM Admin"
admin.site.site_title = "HRM System"
admin.site.index_title = "Department Management Dashboard"

