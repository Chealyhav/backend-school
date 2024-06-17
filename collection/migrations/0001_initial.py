# Generated by Django 3.2.12 on 2024-06-15 15:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Public identifier')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(null=True, upload_to='content')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Staff'), (3, 'User')], default=3, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('background', models.ImageField(blank=True, upload_to='content')),
                ('des', models.CharField(max_length=500, null=True)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('vision_title', models.CharField(max_length=100, null=True)),
                ('vision_des', models.CharField(max_length=200, null=True)),
                ('vision_logo', models.ImageField(blank=True, null=True, upload_to='content')),
                ('mission_title', models.CharField(max_length=100, null=True)),
                ('mission_des', models.CharField(max_length=200, null=True)),
                ('mission_logo', models.ImageField(blank=True, null=True, upload_to='content')),
                ('value_title', models.CharField(max_length=100, null=True)),
                ('value_des', models.CharField(max_length=200, null=True)),
                ('value_logo', models.ImageField(blank=True, null=True, upload_to='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BannerHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.CharField(max_length=500, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('background', models.ImageField(upload_to='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(blank=True, upload_to='content')),
                ('des', models.CharField(max_length=500, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('classCode', models.CharField(max_length=200, null=True)),
                ('background', models.ImageField(blank=True, upload_to='content')),
                ('des', models.CharField(max_length=500, null=True)),
                ('price', models.CharField(max_length=500, null=True)),
                ('duration', models.CharField(max_length=500, null=True)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('sessions', models.CharField(max_length=400, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(blank=True, upload_to='content')),
                ('des', models.CharField(max_length=500, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=500, null=True)),
                ('facebook', models.CharField(max_length=1000, null=True)),
                ('telegram', models.CharField(max_length=1000, null=True)),
                ('instagram', models.CharField(max_length=1000, null=True)),
                ('phone_number', models.CharField(max_length=300, null=True)),
                ('map', models.CharField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groups', models.ManyToManyField(related_name='collection_users', to='auth.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='collection_user', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(related_name='collection_users', to='auth.Permission')),
            ],
        ),
    ]
