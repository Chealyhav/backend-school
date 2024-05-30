

from .models import *
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
# from .serializers import ClaasesSerializer
# from .serializers import TeacherSerializer
# from .serializers import GroupSerializer
# from .serializers import StudentSerializer
# from .serializers import ParentSerializer

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

class SubjectAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                subject = Subject.objects.get(pk=pk)
                serializer = SubjectSerializer(subject)
                return Response(serializer.data)
            except Subject.DoesNotExist:
                return Response({'error': 'Subject record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            subjects = Subject.objects.all()
            serializer = SubjectSerializer(subjects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
            serializer = SubjectSerializer(subject, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
            subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject record not found'}, status=status.HTTP_404_NOT_FOUND)
class ParentAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                parent = Parent.objects.get(pk=pk)
                serializer = ParentSerializer(parent)
                return Response(serializer.data)
            except Parent.DoesNotExist:
                return Response({'error': 'Parent not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            parents = Parent.objects.all()
            serializer = ParentSerializer(parents, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            parent = Parent.objects.get(pk=pk)
            serializer = ParentSerializer(parent, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Parent.DoesNotExist:
            return Response({'error': 'Parent not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            parent = Parent.objects.get(pk=pk)
            parent.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Parent.DoesNotExist:
            return Response({'error': 'Parent not found'}, status=status.HTTP_404_NOT_FOUND)

class AttendanceAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                attendance = Attendance.objects.get(pk=pk)
                serializer = AttendanceSerializer(attendance)
                return Response(serializer.data)
            except Attendance.DoesNotExist:
                return Response({'error': 'Attendance record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            attendance = Attendance.objects.all()
            serializer = AttendanceSerializer(attendance, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            attendance = Attendance.objects.get(pk=pk)
            serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Attendance.DoesNotExist:
            return Response({'error': 'Attendance record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            attendance = Attendance.objects.get(pk=pk)
            attendance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Attendance.DoesNotExist:
            return Response({'error': 'Attendance record not found'}, status=status.HTTP_404_NOT_FOUND)

class ExamTypeAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                exam_type = ExamType.objects.get(pk=pk)
                serializer = ExamTypeSerializer(exam_type)
                return Response(serializer.data)
            except ExamType.DoesNotExist:
                return Response({'error': 'ExamType record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            exam_types = ExamType.objects.all()
            serializer = ExamTypeSerializer(exam_types, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ExamTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            exam_type = ExamType.objects.get(pk=pk)
            serializer = ExamTypeSerializer(exam_type, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ExamType.DoesNotExist:
            return Response({'error': 'ExamType record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            exam_type = ExamType.objects.get(pk=pk)
            exam_type.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExamType.DoesNotExist:
            return Response({'error': 'ExamType record not found'}, status=status.HTTP_404_NOT_FOUND)

class ExamAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                exam = Exam.objects.get(pk=pk)
                serializer = ExamSerializer(exam)
                return Response(serializer.data)
            except Exam.DoesNotExist:
                return Response({'error': 'Exam record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            exams = Exam.objects.all()
            serializer = ExamSerializer(exams, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            exam = Exam.objects.get(pk=pk)
            serializer = ExamSerializer(exam, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exam.DoesNotExist:
            return Response({'error': 'Exam record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            exam = Exam.objects.get(pk=pk)
            exam.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exam.DoesNotExist:
            return Response({'error': 'Exam record not found'}, status=status.HTTP_404_NOT_FOUND)

class ExamResultAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                exam_result = ExamResult.objects.get(pk=pk)
                serializer = ExamResultSerializer(exam_result)
                return Response(serializer.data)
            except ExamResult.DoesNotExist:
                return Response({'error': 'ExamResult record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            exam_results = ExamResult.objects.all()
            serializer = ExamResultSerializer(exam_results, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ExamResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            exam_result = ExamResult.objects.get(pk=pk)
            serializer = ExamResultSerializer(exam_result, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ExamResult.DoesNotExist:
            return Response({'error': 'ExamResult record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            exam_result = ExamResult.objects.get(pk=pk)
            exam_result.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ExamResult.DoesNotExist:
            return Response({'error': 'ExamResult record not found'}, status=status.HTTP_404_NOT_FOUND)

class CourseAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                course = Course.objects.get(pk=pk)
                serializer = CourseSerializer(course)
                return Response(serializer.data)
            except Course.DoesNotExist:
                return Response({'error': 'Course record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({'error': 'Course record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
            course.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Course.DoesNotExist:
            return Response({'error': 'Course record not found'}, status=status.HTTP_404_NOT_FOUND)

class ScoreAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                score = Score.objects.get(pk=pk)
                serializer = ScoreSerializer(score)
                return Response(serializer.data)
            except Score.DoesNotExist:
                return Response({'error': 'Score record not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            scores = Score.objects.all()
            serializer = ScoreSerializer(scores, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            score = Score.objects.get(pk=pk)
            serializer = ScoreSerializer(score, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Score.DoesNotExist:
            return Response({'error': 'Score record not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            score = Score.objects.get(pk=pk)
            score.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Score.DoesNotExist:
            return Response({'error': 'Score record not found'}, status=status.HTTP_404_NOT_FOUND)
class ClassroomAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                classroom = Classroom.objects.get(pk=pk)
                serializer = ClassroomSerializer(classroom)
                return Response(serializer.data)
            except Classroom.DoesNotExist:
                return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            classrooms = Classroom.objects.all()
            serializer = ClassroomSerializer(classrooms, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ClassroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
            serializer = ClassroomSerializer(classroom, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            classroom = Classroom.objects.get(pk=pk)
            classroom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Classroom.DoesNotExist:
            return Response({'error': 'Classroom not found'}, status=status.HTTP_404_NOT_FOUND)