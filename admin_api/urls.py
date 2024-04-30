
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
from django.urls import path
from .views import UserRegistration
from .views import BannerViewSet
from .views import ClassesAPIView
app_name = 'collection'
from django.urls import re_path

urlpatterns = [

    #--- Admin ---#
    re_path(r'^api/banner$', BannerViewSet.as_view(), name='banner-list'),  # GET (list) and POST
    re_path(r'^api/banner/(?P<pk>\d+)$', BannerViewSet.as_view(), name='banner-detail'),
    
    re_path(r'^api/classes$', ClassesAPIView.as_view(), name='classes-list'),  # GET (list) and POST
    re_path(r'^api/classes/(?P<pk>\d+)$', ClassesAPIView.as_view(), name='classes-detail'),
    re_path(r'^api/user$', UserRegistration.as_view(), name='user_register'),
]
