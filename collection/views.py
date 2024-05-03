
import statistics
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View
from django.views import generic
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BannerHomerSerializer
from .models import BannerHome
from .serializers import AboutSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializers, UserLoginSerializer
from .models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import UserLoginSerializer, UserSerializers
from .models import User

# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializers

class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=request.data['username'])
        
        if not user.check_password(request.data['password']):
            return Response("Invalid username or password", status=status.HTTP_401_UNAUTHORIZED)
        
        token, created = Token.objects.get_or_create(user=user)
        
        response = {
            'success': True,
            'statusCode': status.HTTP_200_OK,
            'message': 'User logged in successfully',
            'token': token.key,
            'email': user.email,
            'role': user.role
        }

        return Response(response)

class UserList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    serializer_class = UserSerializers
    def get_queryset(self):
        return User.objects.all()
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        response = {
            'success': True,
            'statusCode': status.HTTP_201_CREATED,
            'message': 'User created successfully',
            'token': token.key,
            'email': user.email,
            'role': user.role
        }

        return Response(response, status=status.HTTP_201_CREATED)

# class SignupView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = User.objects.get(username=request.data['username'])
#             user.set_password(request.data['password'])
#             user.save()
#             token = Token.objects.create(user=user)
#             return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginView(APIView):
#     def post(self, request):
#         user = get_object_or_404(User, username=request.data['username'])
#         if not user.check_password(request.data['password']):
#             return Response("Invalid username or password", status=status.HTTP_404_NOT_FOUND)
#         token, created = Token.objects.get_or_create(user=user)
#         serializer = UserSerializer(user)
#         return Response({'token': token.key, 'user': serializer.data})

class TestTokenView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response("Passed!")



class BannerHomeAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            banner = BannerHome.objects.get(pk=pk)
            serializer = BannerHomerSerializer(banner)
            return Response(serializer.data)
        else:
            banners = BannerHome.objects.all()
            serializer = BannerHomerSerializer(banners, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BannerHomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def patch(self, request, pk):
        try:
            banner = BannerHome.objects.get(pk=pk)
        except BannerHome.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        image_path = os.path.join('media', str(banner.background))
        if os.path.exists(image_path):
            os.remove(image_path)

        serializer = BannerHomerSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            banner = BannerHome.objects.get(pk=pk)
            image_path = os.path.join('media', str(banner.background))
            if os.path.exists(image_path):
                os.remove(image_path)
                banner.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except BannerHome.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)


 
class AboutAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            about = About.objects.get(pk=pk)
            serializer = AboutSerializer(about)
            return Response(serializer.data)
        else:
            about = About.objects.all()
            serializer = AboutSerializer(about, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            about = About.objects.get(pk=pk)
        except About.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            image = About.objects.get(pk=pk)
            image_path = os.path.join('media', str(image.image))
            if os.path.exists(image_path):
                os.remove(image_path)
                image.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except About.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)



class LogoAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            banner = self.get_logo(pk)
            if banner:
                serializer = LogoSerializer(banner)
                return Response(serializer.data)
            return Response({'error': 'Logo not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            banners = Logo.objects.all()
            serializer = LogoSerializer(banners, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = LogoSerializer(data=request.data)
        if serializer.is_valid():
            logo = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        banner = self.get_logo(pk)
        if banner:
            serializer = LogoSerializer(banner, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Logo not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        banner = self.get_logo(pk)
        if banner:
            banner.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Logo not found'}, status=status.HTTP_404_NOT_FOUND)

    def get_logo(self, pk):
        try:
            banner = Logo.objects.get(pk=pk)
            return banner
        except Logo.DoesNotExist:
            return None