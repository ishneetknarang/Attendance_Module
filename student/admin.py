from django.contrib import admin
from .models import Student, Faculty, Attendance

# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Attendance)
