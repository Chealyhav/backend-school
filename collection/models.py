from django.db import models
from django.core.exceptions import ValidationError
import os
from django_ckeditor_5.fields import CKEditor5Field
from rest_framework.authtoken.models import Token





class BannerHome(models.Model):
    des = models.CharField(max_length=500,null=True)
    title = models.CharField(max_length=100,null=True)
    subtitle = models.CharField(max_length=100,null=True)
    background = models.ImageField(upload_to='content')
    def __str__(self):
        return self.title


class Logo(models.Model):
    background = models.CharField(max_length=500)
    title = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.background


class Strategy(models.Model):
    icon = models.ImageField(upload_to='content',null=True)
    des = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=200, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.title    

class About(models.Model):
    title = models.CharField(max_length=200, null=True)
    background = models.ImageField(upload_to='content', blank=True)
    des = models.CharField(max_length=500, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    # vision_title = models.CharField(max_length=100, null=True)
    # vision_des = models.CharField(max_length=200, null=True)
    # vision_logo = models.ImageField(upload_to='content', blank=True,null=True)
    # mission_title = models.CharField(max_length=100, null=True)
    # mission_des = models.CharField(max_length=200, null=True)
    # mission_logo = models.ImageField(upload_to='content', blank=True,null=True)
    # value_title = models.CharField(max_length=100, null=True)
    # value_des = models.CharField(max_length=200, null=True)
    # value_logo = models.ImageField(upload_to='content', blank=True,null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title





