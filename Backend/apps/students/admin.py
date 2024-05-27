from django.contrib import admin
from .models import StudentList, Departments, Branches


# Register your models here.

admin.site.register(Branches)
admin.site.register(Departments)
admin.site.register(StudentList)
