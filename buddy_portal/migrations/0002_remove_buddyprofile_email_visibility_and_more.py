# Generated by Django 5.1.4 on 2025-01-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_portal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buddyprofile',
            name='email_visibility',
        ),
        migrations.AddField(
            model_name='buddyprofile',
            name='show_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='buddyprofile',
            name='show_phone',
            field=models.BooleanField(default=True),
        ),
    ]
