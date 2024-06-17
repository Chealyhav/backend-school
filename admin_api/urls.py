

from django.urls import  re_path
from .views import *
app_name = 'collection'
urlpatterns = [

    re_path(r'^api/classes$', ClassesAPIView.as_view(), name='classes-list'),  # GET (list) and POST
    re_path(r'^api/classes/(?P<pk>\d+)$', ClassesAPIView.as_view(), name='classes-detail'),
    
    re_path(r'^api/teacher$', TeacherViewSet.as_view(), name='teacher-list'),  # GET (list) and POST
    re_path(r'^api/teacher/(?P<pk>\d+)$', TeacherViewSet.as_view(), name='teacher-detail'),
    
    re_path(r'^api/student$', StudentAPIView.as_view(), name='student-list'),  # GET (list) and POST
    re_path(r'^api/student/(?P<pk>\d+)$', StudentAPIView.as_view(), name='student-detail'),
    

    re_path(r'^api/parent$', ParentAPIView.as_view(), name='parent-list'),  # GET (list) and POST
    re_path(r'^api/parent/(?P<pk>\d+)$', ParentAPIView.as_view(), name='parent-detail'),  # GET, PATCH, DELETE
    

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
    
    
    re_path(r'^api/scores$', ScoreAPIView.as_view(), name='score-list'),  # GET (list) and POST
    re_path(r'^api/scores/(?P<pk>\d+)$', ScoreAPIView.as_view(), name='score-detail'),  # GET, PATCH, DELETE
]
