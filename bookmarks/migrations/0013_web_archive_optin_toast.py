# Generated by Django 3.2.6 on 2022-01-08 19:27

from django.db import migrations
from django.contrib.auth import get_user_model

from bookmarks.models import Toast

User = get_user_model()


def forwards(apps, schema_editor):
    for user in User.objects.all():
        toast = Toast(key='web_archive_opt_in_hint',
                      message='The Internet Archive Wayback Machine integration has been disabled by default. Check the Settings to re-enable it.',
                      owner=user)
        toast.save()


def reverse(apps, schema_editor):
    Toast.objects.filter(key='web_archive_opt_in_hint').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('bookmarks', '0012_toast'),
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
