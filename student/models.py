from django.db import models
from django.utils import timezone
# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length = 100)# models.ForeignKey('auth.User', on_delete=models.CASCADE)
    last_name = models.CharField(max_length = 100)
    student_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name +" "+self.last_name


class Faculty(models.Model):
    first_name = models.CharField(max_length = 100)# models.ForeignKey('auth.User', on_delete=models.CASCADE)
    last_name = models.CharField(max_length = 100)
    faculty_id = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100,default=faculty_id)
    password = models.CharField(max_length = 50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name +" "+self.last_name

    class Meta:
        verbose_name_plural = "Faculties"


class Attendance(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.localdate())
    status= models.BooleanField(default=0)

    def __str__(self):
        return self.student.first_name + str(self.date)

