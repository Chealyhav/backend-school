# Generated by Django 3.2.12 on 2024-05-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0003_alter_student_studentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(default='AP', max_length=10),
        ),
    ]