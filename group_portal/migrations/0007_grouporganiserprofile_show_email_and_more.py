# Generated by Django 5.1.4 on 2025-01-16 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_portal', '0006_alter_group_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouporganiserprofile',
            name='show_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='grouporganiserprofile',
            name='show_phone',
            field=models.BooleanField(default=True),
        ),
    ]
