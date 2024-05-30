
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
from django.urls import path
# from .views import ClassesAPIView
# from .views import TeacherViewSet
# from .views import GroupAPIView
# from .views import StudentAPIView
# from .views import ParentAPIView
app_name = 'collection'
from django.urls import re_path

urlpatterns = [

    re_path(r'^api/classes$', ClassesAPIView.as_view(), name='classes-list'),  # GET (list) and POST
    re_path(r'^api/classes/(?P<pk>\d+)$', ClassesAPIView.as_view(), name='classes-detail'),
    
    re_path(r'^api/teacher$', TeacherViewSet.as_view(), name='teacher-list'),  # GET (list) and POST
    re_path(r'^api/teacher/(?P<pk>\d+)$', TeacherViewSet.as_view(), name='teacher-detail'),
    
    re_path(r'^api/student$', StudentAPIView.as_view(), name='student-list'),  # GET (list) and POST
    re_path(r'^api/student/(?P<pk>\d+)$', StudentAPIView.as_view(), name='student-detail'),
    
    re_path(r'^api/group$', GroupAPIView.as_view(), name='group-list'),  # GET (list) and POST
    re_path(r'^api/group/(?P<pk>\d+)$', GroupAPIView.as_view(), name='group-detail'),
    
    re_path(r'^api/parent$', ParentAPIView.as_view(), name='parent-list'),  # GET (list) and POST
    re_path(r'^api/parent/(?P<pk>\d+)$', ParentAPIView.as_view(), name='parent-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/classroom$', ClassroomAPIView.as_view(), name='classroom-list'),  # GET (list) and POST
    re_path(r'^api/classroom/(?P<pk>\d+)$', ClassroomAPIView.as_view(), name='classroom-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/attendance$', AttendanceAPIView.as_view(), name='attendance-list'),  # GET (list) and POST
    re_path(r'^api/attendance/(?P<pk>\d+)$', AttendanceAPIView.as_view(), name='attendance-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/exam-types$', ExamTypeAPIView.as_view(), name='examtype-list'),  # GET (list) and POST
    re_path(r'^api/exam-types/(?P<pk>\d+)$', ExamTypeAPIView.as_view(), name='examtype-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/exams$', ExamAPIView.as_view(), name='exam-list'),  # GET (list) and POST
    re_path(r'^api/exams/(?P<pk>\d+)$', ExamAPIView.as_view(), name='exam-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/subjects$', SubjectAPIView.as_view(), name='subject-list'),  # GET (list) and POST
    re_path(r'^api/subjects/(?P<pk>\d+)$', SubjectAPIView.as_view(), name='subject-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/exam-results$', ExamResultAPIView.as_view(), name='examresult-list'),  # GET (list) and POST
    re_path(r'^api/exam-results/(?P<pk>\d+)$', ExamResultAPIView.as_view(), name='examresult-detail'),  # GET, PATCH, DELETE
    
    re_path(r'^api/courses$', CourseAPIView.as_view(), name='course-list'),  # GET (list) and POST
    re_path(r'^api/courses/(?P<pk>\d+)$', CourseAPIView.as_view(), name='course-detail'),  # GET, PATCH, DELETE

    re_path(r'^api/scores$', ScoreAPIView.as_view(), name='score-list'),  # GET (list) and POST
    re_path(r'^api/scores/(?P<pk>\d+)$', ScoreAPIView.as_view(), name='score-detail'),  # GET, PATCH, DELETE
]
