from .models import * 
from rest_framework import serializers
from django.contrib.auth.models import User


from .models import User
from django.contrib.auth import authenticate



#creating serializers.


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","first_name", "last_name","password" ,"username", "role","token"]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            token=validated_data['token']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    role = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']
        token=data['token']
        user = authenticate(email=email, password=password,token=token)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
         
            validation = {
                'email': user.email,
                "password": user.password,
                'role': user.role,
                'token': user.token,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")
# class UserSerializer(serializers.ModelSerializer): 
#     class Meta: 
#         model = User 
#         fields = ['username', 'password']
#     def create(self, validated_data): 
#         user = User.objects.create(username=validated_data['username'])
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
class BannerHomerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = BannerHome 
        fields = '__all__'    
        
class LogoSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Logo 
        fields = '__all__'    

# class StrategySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Strategy
#         fields = '__all__'
        
        
class AboutSerializer(serializers.ModelSerializer):
    # strategy = StrategySerializer(many=True)

    class Meta:
        model = About
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Blog 
        fields = '__all__'  
class ContactSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Contact 
        fields = '__all__'          
