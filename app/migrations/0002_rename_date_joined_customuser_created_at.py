# Generated by Django 3.2.9 on 2021-12-09 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='date_joined',
            new_name='created_at',
        ),
    ]
