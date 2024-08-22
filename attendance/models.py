# models.py
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User # Import your custom User model from the 'accounts' app

from django.contrib.auth.models import User

# ...

class Student(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10)
def __str__(self):
    return self.user.username

class Class(models.Model):
    name = models.CharField(max_length=100)

class Attendance(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    class_attended = models.OneToOneField(Class, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField()
