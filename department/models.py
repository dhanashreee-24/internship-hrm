from django.db import models

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)  # True = Active, False = Inactive

    def __str__(self):
        return self.dept_name
