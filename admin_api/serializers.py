from .models import * 
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['username', 'password']
    def create(self, validated_data): 
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user
        
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