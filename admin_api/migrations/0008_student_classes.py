# Generated by Django 3.2.12 on 2024-06-12 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_api', '0007_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_api.classes'),
        ),
    ]
