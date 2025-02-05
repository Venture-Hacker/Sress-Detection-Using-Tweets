# Generated by Django 4.1 on 2023-02-25 08:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stressapp', '0013_alter_registration_email_alter_registration_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='password',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='username',
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
