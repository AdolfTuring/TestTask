# Generated by Django 3.2 on 2021-04-23 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userblog', '0008_alter_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post',
        ),
    ]
