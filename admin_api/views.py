

from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from .serializers import ClaasesSerializer
from .serializers import TeacherSerializer
from .serializers import GroupSerializer
from .serializers import StudentSerializer
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

class TeacherViewSet(APIView):
    def get(self, request, pk=None):
        if pk:
            teacher = Teacher.objects.get(pk=pk)
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        else:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk):
        try:
            image = Teacher.objects.get(pk=pk)
            serializer = TeacherSerializer(image, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Teacher.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            image = Teacher.objects.get(pk=pk)
            image_path = os.path.join('media', str(image.profile))
            if os.path.exists(image_path):
                os.remove(image_path)
                image.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except Teacher.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)

class GroupAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                group = Group.objects.get(pk=pk)
                serializer = GroupSerializer(group)
                return Response(serializer.data)
            except Group.DoesNotExist:
                return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            groups = Group.objects.all()
            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            serializer = GroupSerializer(group, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Group.DoesNotExist:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Group.DoesNotExist:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
class StudentAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            image = Student.objects.get(pk=pk)
            serializer = StudentSerializer(image, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        try:
            image = Student.objects.get(pk=pk)
            image_path = os.path.join('media', str(image.background))
            if os.path.exists(image_path):
                os.remove(image_path)
                image.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Image file not found'}, status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
            return Response({'error': 'Image not found'}, status=status.HTTP_404_NOT_FOUND)


