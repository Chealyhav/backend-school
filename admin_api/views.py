
from django.contrib.auth.models import User
from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from .models import Banner
# from .serializers import BannerSerializer
import os
class UserRegistration(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        # This is just an example. You can customize the GET method as needed.
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClassesAPIView(APIView):
    def get(self, request, pk=None):
        if pk:
            classes = Classes.objects.get(pk=pk)
            serializer = ClaasesSerializer(classes)
            return Response(serializer.data)
        else:
            classes = Classes.objects.all()
            serializer = ClaasesSerializer(classes, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ClaasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def patch(self, request, pk):
    #     try:
    #         classes = Classes.objects.get(pk=pk)
    #     except Classes.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     serializer = ClaasesSerializer(classes, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     try:
    #         classes = Classes.objects.get(pk=pk)
    #     except Classes.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     classes.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk):
        try:
            classes = Classes.objects.get(pk=pk)
            serializer = ClaasesSerializer(classes, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Classes.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            classes = Classes.objects.get(pk=pk)
            image_path = os.path.join('media', str(classes.background))
            if os.path.exists(image_path):
                os.remove(image_path)
                classes.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except Classes.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

class BannerViewSet(APIView):
    def get(self, request, pk=None):
        if pk:
            about = Banner.objects.get(pk=pk)
            serializer = BannerSerializer(about)
            return Response(serializer.data)
        else:
            about = Banner.objects.all()
            serializer = BannerSerializer(about, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            image = Banner.objects.get(pk=pk)
            serializer = BannerSerializer(image, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Banner.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            image = Banner.objects.get(pk=pk)
            image_path = os.path.join('media', str(image.image))
            if os.path.exists(image_path):
                os.remove(image_path)
                image.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except Banner.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

