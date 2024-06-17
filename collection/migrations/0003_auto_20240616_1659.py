# Generated by Django 3.2.12 on 2024-06-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('collection', '0002_auto_20240616_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionuser',
            name='groups',
            field=models.ManyToManyField(related_name='collection_users', to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='collectionuser',
            name='user_permissions',
            field=models.ManyToManyField(related_name='collection_users', to='auth.Permission'),
        ),
    ]
