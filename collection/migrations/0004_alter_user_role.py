# Generated by Django 5.0.1 on 2024-05-03 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_remove_user_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('Admin', 'Admin'), ('Staff', 'Staff'), ('User', 'User')], default='User', null=True),
        ),
    ]
