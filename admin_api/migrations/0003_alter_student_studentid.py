# Generated by Django 3.2.12 on 2024-05-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0002_auto_20240530_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentID',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]
