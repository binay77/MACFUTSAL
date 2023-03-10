# Generated by Django 4.1.1 on 2023-01-02 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassCoordinator', '0002_rename_title_team_registration_team_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_registration',
            name='Captain',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_registration',
            name='Defender_1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_registration',
            name='Defender_2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_registration',
            name='Manager',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_registration',
            name='Striker_1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_registration',
            name='Striker_2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team_registration',
            name='Substitutes',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team_registration',
            name='Goal_Keeper',
            field=models.CharField(max_length=50),
        ),
    ]
