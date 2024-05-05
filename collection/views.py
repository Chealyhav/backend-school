
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

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class AuthUserLoginView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'email': serializer.data['email'],
                'role': serializer.data['role'],
                'email': serializer.data['email'],
                'username':serializer.data['username'],
                'first_name':serializer.data['first_name'],
                'last_name':serializer.data['last_name'],
            }

            return Response(response, status=status_code)



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
            image_path = os.path.join('media', str(image.background))
            if os.path.exists(image_path):
                os.remove(image_path)
                image.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except About.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

class BlogAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                blog = Blog.objects.get(pk=pk)
                serializer = BlogSerializer(blog)
                return Response(serializer.data)
            except Blog.DoesNotExist:
                return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            banner = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        image_path = os.path.join('media', str(banner.background))
        if os.path.exists(image_path):
            os.remove(image_path)

        serializer = BlogSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            banner = Blog.objects.get(pk=pk)
            image_path = os.path.join('media', str(banner.background))
            if os.path.exists(image_path):
                os.remove(image_path)
                banner.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except Blog.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

class ContactAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                contact = Contact.objects.get(pk=pk)
                serializer = ContactSerializer(contact)
                return Response(serializer.data)
            except Contact.DoesNotExist:
                return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        image_path = os.path.join('media', str(contact.background))
        if os.path.exists(image_path):
            os.remove(image_path)

        serializer = ContactSerializer(contact, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            contact = Contact.objects.get(pk=pk)
            image_path = os.path.join('media', str(contact.background))
            if os.path.exists(image_path):
                os.remove(image_path)
            contact.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contact.DoesNotExist:
            return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)

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

    def patch(self, request, pk):
        try:
            banner = Logo.objects.get(pk=pk)
        except Logo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        image_path = os.path.join('media', str(banner.background))
        if os.path.exists(image_path):
            os.remove(image_path)

        serializer = LogoSerializer(banner, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            banner = Logo.objects.get(pk=pk)
            image_path = os.path.join('media', str(banner.background))
            if os.path.exists(image_path):
                os.remove(image_path)
                banner.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except Logo.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)