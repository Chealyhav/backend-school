
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
from django.urls import path

from .views import BannerHomeAPIView
from .views import LogoAPIView
from .views import UserRegistration
from .views import AboutAPIView

app_name = 'collection'
from django.urls import re_path


urlpatterns = [
    re_path(r'^api/logo$', LogoAPIView.as_view(), name='home-list'),  # GET (list) and POST
    re_path(r'^api/logo/(?P<pk>\d+)$', LogoAPIView.as_view(), name='home-detail'),  # GET (detail), PUT, and DELETE
    re_path(r'^api/bannerhome$', BannerHomeAPIView.as_view(), name='home-list'),  # GET (list) and POST
    re_path(r'^api/bannerhome/(?P<pk>\d+)$', BannerHomeAPIView.as_view(), name='home-detail'),  # GET (detail), PUT, and DELETE
    re_path(r'^api/about$', AboutAPIView.as_view(), name='about-list'),  # GET (list) and POST
    re_path(r'^api/about/(?P<pk>\d+)$', AboutAPIView.as_view(), name='about-detail'),
     
    # re_path(r'^api/classes$', ClassesAPIView.as_view(), name='classes-list'),  # GET (list) and POST
    # re_path(r'^api/classes/(?P<pk>\d+)$', ClassesAPIView.as_view(), name='classes-detail'),
    re_path(r'^api/user$', UserRegistration.as_view(), name='user_register'),
    re_path(r'^api/user/(?P<pk>\d+)$', UserRegistration.as_view(), name='user_register-detail'),
]


