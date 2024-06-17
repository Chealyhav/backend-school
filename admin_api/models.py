from django.db import models
from django.core.exceptions import ValidationError
import os
from rest_framework.authtoken.models import Token


# school management system 
class Parent(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length=200, null=True)
    classCode = models.CharField(max_length=200, null=True)
    background = models.ImageField(upload_to='content', blank=True)
    des = models.CharField(max_length=500, null=True)
    price = models.CharField(max_length=500, null=True)
    duration = models.CharField(max_length=500, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    sessions = models.CharField(max_length=400, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    studentID = models.CharField(max_length=255, unique=True, blank=True)
    profile = models.ImageField(upload_to='content', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True) 
    def __str__(self):
        return f"{self.firstName} {self.lastName}"
    def save(self, *args, **kwargs):
        if not self.studentID:
            last_student = Student.objects.all().order_by('id').last()
            if last_student and last_student.studentID.isdigit():
                last_id = int(last_student.studentID)
                new_id = last_id + 1
            else:
                new_id = 1
            self.studentID = str(new_id).zfill(3) 
        super(Student, self).save(*args, **kwargs)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, default="P")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.student.name} - {self.date}"

class ExamType(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=100)
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=20)
    des = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.student.name} - {self.exam.name} - {self.subject.name}"

class Teacher(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    subject = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=255, null=True)
    registrationDate = models.DateField(null=True)
    phone = models.CharField(max_length=255, null=True)
    experience = models.CharField(max_length=500, null=True)
    profile = models.ImageField(upload_to='content', blank=True, null=True)
    classes = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"

class Score(models.Model):
    title = models.CharField(max_length=120)
    student = models.ForeignKey(Student, related_name='scores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class Session(models.Model):
    title = models.CharField(max_length=120)
    subject = models.ForeignKey(Subject, related_name='scores', on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, related_name='scores', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
