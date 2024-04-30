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
    
class BannerHomerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = BannerHome 
        fields = '__all__'    
        
class LogoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Logo 
        fields = '__all__'    

class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = '__all__'
        
        
class AboutSerializer(serializers.ModelSerializer):
    # strategy = StrategySerializer(many=True)

    class Meta:
        model = About
        fields = '__all__'


        
