from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in Department._meta.fields]


admin.site.site_header = "HRM Admin"
admin.site.site_title = "HRM System"
admin.site.index_title = "Department Management Dashboard"
