# Generated by Django 2.2.7 on 2019-11-24 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_instructor',
        ),
    ]
