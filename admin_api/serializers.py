from .models import * 
from rest_framework import serializers
from django.contrib.auth.models import User

class ClaasesSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Classes 
        fields = '__all__' 
        
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'