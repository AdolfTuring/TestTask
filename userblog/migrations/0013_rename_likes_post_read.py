# Generated by Django 3.2 on 2021-04-24 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userblog', '0012_auto_20210424_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='read',
        ),
    ]
