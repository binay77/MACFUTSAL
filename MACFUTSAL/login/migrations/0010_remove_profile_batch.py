# Generated by Django 4.1.1 on 2023-02-18 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_profile_batch_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='batch',
        ),
    ]
