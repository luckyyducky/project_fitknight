# Generated by Django 5.1.4 on 2025-01-13 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy_portal', '0003_alter_buddyprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buddyprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
