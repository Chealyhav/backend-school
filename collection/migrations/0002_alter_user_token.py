# Generated by Django 5.0.1 on 2024-05-03 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]