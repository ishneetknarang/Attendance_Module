# Generated by Django 2.0.3 on 2018-08-08 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='faculty_id',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='password',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='username',
        ),
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AddField(
            model_name='faculty',
            name='faculty',
            field=models.OneToOneField(default=0.010907288051561725, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
