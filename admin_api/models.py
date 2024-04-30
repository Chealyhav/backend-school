from django.db import models
from django.core.exceptions import ValidationError
import os
from rest_framework.authtoken.models import Token
from django.db import models
from django.db import models

from django.db import models

class Classes(models.Model):
    name = models.CharField(max_length=200, null=True)
    classCode = models.CharField(max_length=200, null=True)
    background = models.ImageField(upload_to='content', null=True)
    des = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=500, null=True)
    duration = models.CharField(max_length=500, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    sessions = models.CharField(max_length=400, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


    
class Teacher(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=100, null=True)
    dob = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    registrationDate = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    experience = models.CharField(max_length=500, null=True)
    profile = models.ImageField(upload_to='content', blank=True, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, null=True)
    dob = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    registrationDate = models.DateField(max_length=100, null=True)
    phone = models.CharField(max_length=255, null=True)
    studentID = models.CharField(max_length=255)
    profile = models.ImageField(upload_to='content', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, related_name='student_score', on_delete=models.CASCADE)
    classes = models.ManyToManyField(Classes)
    
    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Course(models.Model): 
    title = models.CharField(max_length=120)
    activate = models.BooleanField(default=True)
    def __str__(self) -> str:
        return str(self.title)

class Score(models.Model): 
    title = models.CharField(max_length=120)
    student = models.ForeignKey(Student, related_name='student_score', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='course_score', on_delete = models.CASCADE)
    activate = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.title
 
 
    
class Banner(models.Model):
    # title = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='content')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title