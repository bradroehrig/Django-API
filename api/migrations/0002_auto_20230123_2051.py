# Generated by Django 2.2.4 on 2023-01-24 02:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
    ]
