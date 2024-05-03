import uuid
from django.db import models
import os
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.tokens import default_token_generator
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN = 1
    STAFF = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (STAFF, 'Staff'),
        (USER, 'User')
    )
    
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=USER)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    token = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class CollectionUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='collection_user')
    groups = models.ManyToManyField(Group, related_name='collection_users')
    user_permissions = models.ManyToManyField(Permission, related_name='collection_users')

    def __str__(self):
        return self.user.username





class BannerHome(models.Model):
    des = models.CharField(max_length=500,null=True)
    title = models.CharField(max_length=100,null=True)
    subtitle = models.CharField(max_length=100,null=True)
    background = models.ImageField(upload_to='content')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Logo(models.Model):
    background = models.CharField(max_length=500)
    title = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.background

class About(models.Model):
    title = models.CharField(max_length=200, null=True)
    background = models.ImageField(upload_to='content', blank=True)
    des = models.CharField(max_length=500, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    vision_title = models.CharField(max_length=100, null=True)
    vision_des = models.CharField(max_length=200, null=True)
    vision_logo = models.ImageField(upload_to='content', blank=True,null=True)
    mission_title = models.CharField(max_length=100, null=True)
    mission_des = models.CharField(max_length=200, null=True)
    mission_logo = models.ImageField(upload_to='content', blank=True,null=True)
    value_title = models.CharField(max_length=100, null=True)
    value_des = models.CharField(max_length=200, null=True)
    value_logo = models.ImageField(upload_to='content', blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Blog(models.Model):
    background = models.ImageField(upload_to='content', blank=True)
    des = models.CharField(max_length=500,null=True)
    title = models.CharField(max_length=100,null=True)
    subtitle = models.CharField(max_length=100,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.background

class Contact(models.Model):
    background = models.ImageField(upload_to='content', blank=True)
    des = models.CharField(max_length=500,null=True)
    title = models.CharField(max_length=100,null=True)
    subtitle = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=500,null=True)
    facebook = models.CharField(max_length=1000,null=True)
    telegram = models.CharField(max_length=1000,null=True)
    instagram = models.CharField(max_length=1000,null=True)
    phone_number = models.CharField(max_length=300,null=True)
    map = models.CharField(max_length=1000,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.background

