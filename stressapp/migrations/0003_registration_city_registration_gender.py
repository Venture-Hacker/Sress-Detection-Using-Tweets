# Generated by Django 4.1 on 2022-08-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stressapp', '0002_rename_age_registration_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
