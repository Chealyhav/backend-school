
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings 
from django.conf.urls.static import static
from .views import *
from django.urls import path
from .views import BannerHomeAPIView
from .views import LogoAPIView
from .views import AboutAPIView
from .views import BlogAPIView
from .views import ContactAPIView
from .views import UserList, AuthUserLoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'collection'
from django.urls import re_path


urlpatterns = [
    re_path(r'^api/logo$', LogoAPIView.as_view(), name='home-list'),  # GET (list) and POST
    re_path(r'^api/logo/(?P<pk>\d+)$', LogoAPIView.as_view(), name='home-detail'),  # GET (detail), PUT, and DELETE
    re_path(r'^api/bannerhome$', BannerHomeAPIView.as_view(), name='home-list'),  # GET (list) and POST
    re_path(r'^api/bannerhome/(?P<pk>\d+)$', BannerHomeAPIView.as_view(), name='home-detail'),  # GET (detail), PUT, and DELETE
    re_path(r'^api/about$', AboutAPIView.as_view(), name='about-list'),  # GET (list) and POST
    re_path(r'^api/about/(?P<pk>\d+)$', AboutAPIView.as_view(), name='about-detail'),
    re_path(r'^api/blog$', BlogAPIView.as_view(), name='blog-list'),  # GET (list) and POST
    re_path(r'^api/blog/(?P<pk>\d+)$', BlogAPIView.as_view(), name='blog-detail'), 
    re_path(r'^api/contact$', ContactAPIView.as_view(), name='contact-list'),  # GET (list) and POST
    re_path(r'^api/contact/(?P<pk>\d+)$', ContactAPIView.as_view(), name='contact-detail'),
    re_path(r'^api/banner$', BannerViewSet.as_view(), name='banner-list'),  # GET (list) and POST
    re_path(r'^api/banner/(?P<pk>\d+)$', BannerViewSet.as_view(), name='banner-detail'),
    
     
    
    re_path(r'^api/register$', UserList.as_view(), name = "register"),
    re_path(r'^api/login$', AuthUserLoginView.as_view(), name = "login"),
    re_path(r'^api/token$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


