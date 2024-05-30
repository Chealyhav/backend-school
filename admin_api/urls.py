
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
from django.urls import path
from .views import ClassesAPIView
from .views import TeacherViewSet
from .views import GroupAPIView
from .views import StudentAPIView
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
]
