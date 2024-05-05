# Generated by Django 5.0.1 on 2024-05-03 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
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
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('activate', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('dob', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('registrationDate', models.DateField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('studentID', models.CharField(max_length=255)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ManyToManyField(to='admin_api.classes')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_score', to='admin_api.group')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('activate', models.BooleanField(default=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_score', to='admin_api.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_score', to='admin_api.student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('dob', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('registrationDate', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('experience', models.CharField(max_length=500, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('classes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_api.classes')),
            ],
        ),
    ]
